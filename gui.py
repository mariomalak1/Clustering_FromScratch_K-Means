import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import main

class K_Means_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("K-Means Clustering")
        self.root.geometry("1000x700")

        self.filename_var = tk.StringVar()
        self.percentage_var = tk.IntVar(value=100)
        self.k_var = tk.IntVar(value=3)

        self.clusters = None
        self.num_iterations = None
        self.dataLabels = None
        self.realDataAfterClustreing = None
        self.outliers = None

        self.create_widgets()

    def create_widgets(self):
        input_frame = ttk.LabelFrame(self.root, text="Input Parameters", padding=10)
        input_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(input_frame, text="File:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(input_frame, textvariable=self.filename_var, width=70).grid(row=0, column=1, padx=5)
        ttk.Button(input_frame, text="Browse", command=self.browse_file).grid(row=0, column=2)

        ttk.Label(input_frame, text="Percentage of rows (%):").grid(row=1, column=0, sticky=tk.W)
        tk.Scale(input_frame,
                 from_=1,
                 to=100,
                 variable=self.percentage_var,
                 orient=tk.HORIZONTAL,
                 resolution=1).grid(row=1, column=1, sticky=tk.EW, padx=5)
        ttk.Label(input_frame, textvariable=self.percentage_var).grid(row=1, column=2)

        ttk.Label(input_frame, text="Number of clusters (k):").grid(row=2, column=0, sticky=tk.W)
        ttk.Spinbox(input_frame, from_=1, to=20, textvariable=self.k_var, width=5).grid(row=2, column=1, sticky=tk.W,
                                                                                        padx=5)

        ttk.Button(input_frame, text="Run K-Means", command=self.run_kmeans).grid(row=3, column=1, pady=10)

        self.results_frame = ttk.Frame(self.root)
        self.results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.notebook = ttk.Notebook(self.results_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

    def displayOutliers(self):
        # tab to get all outliers
        outliers_tab = ttk.Frame(self.notebook)
        self.notebook.add(outliers_tab, text="Outliers")

        outliers_frame = ttk.Frame(outliers_tab)
        outliers_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(outliers_frame, text="Detected Outliers",
                  font=('Arial', 12, 'bold')).pack(pady=(0, 10))

        if hasattr(self, 'outliers') and self.outliers:
            tree_container = ttk.Frame(outliers_frame)
            tree_container.pack(fill=tk.BOTH, expand=True)

            tree = ttk.Treeview(tree_container, columns=self.dataLabels, show="headings", height=10)

            for col in self.dataLabels:
                tree.heading(col, text=col)
                tree.column(col, width=100, anchor=tk.CENTER)

            scroll_y = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scroll_y.set)

            # Pack tree and vertical scrollbar
            tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

            # Horizontal scrollbar
            scroll_x = ttk.Scrollbar(tree, orient="horizontal", command=tree.xview)
            tree.configure(xscrollcommand=scroll_x.set)
            scroll_x.pack(fill=tk.X, side=tk.BOTTOM)

            for point in self.outliers:
                tree.insert("", tk.END, values=point)

            ttk.Label(outliers_frame,
                      text=f"Total outliers detected: {len(self.outliers)}",
                      font=('Arial', 10)).pack(pady=(10, 0), anchor="w")
        else:
            ttk.Label(outliers_frame,
                      text="No outliers detected",
                      font=('Arial', 11)).pack(pady=20)

    def browse_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.filename_var.set(filename)

    def run_kmeans(self):
        if not self.filename_var.get():
            messagebox.showerror("Error", "Please select a file first")
            return

        try:
            self.clusters, self.num_iterations, self.realDataAfterClustreing, self.outliers, self.dataLabels = main.main(
                self.filename_var.get(),
                self.percentage_var.get(),
                self.k_var.get()
            )

            self.displayResults()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            print(e)

    def displayResults(self):
        for child in self.notebook.winfo_children():
            child.destroy()

        counter = 0
        for cluster in self.clusters:
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=f"{cluster.getName()}")

            content_frame = ttk.Frame(tab)
            content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            info_frame = ttk.LabelFrame(content_frame, text="Cluster Information", padding=10)
            info_frame.pack(fill=tk.X, pady=5)

            ttk.Label(info_frame, text=f"Centroid: {cluster.getCurrentLocation()}").pack(anchor=tk.W)
            ttk.Label(info_frame, text=f"Number of points: {len(cluster.getClusterPoints())}").pack(anchor=tk.W)

            points_frame = ttk.LabelFrame(content_frame, text="Points in Cluster", padding=10)
            points_frame.pack(fill=tk.BOTH, expand=True)

            tree = ttk.Treeview(points_frame, columns=self.dataLabels, show="headings")

            for col in self.dataLabels:
                tree.heading(col, text=col)
                tree.column(col, width=100)

            # add points to the treeview
            for point in self.realDataAfterClustreing[counter]:
                tree.insert("", tk.END, values=point)

            # add scrollbars
            vsb = ttk.Scrollbar(points_frame, orient="vertical", command=tree.yview)
            hsb = ttk.Scrollbar(points_frame, orient="horizontal", command=tree.xview)
            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

            tree.grid(row=0, column=0, sticky=tk.NSEW)
            vsb.grid(row=0, column=1, sticky=tk.NS)
            hsb.grid(row=1, column=0, sticky=tk.EW)

            points_frame.grid_rowconfigure(0, weight=1)
            points_frame.grid_columnconfigure(0, weight=1)
            counter += 1

        # tab that hold num of iterations, and number of clusters
        summary_tab = ttk.Frame(self.notebook)
        self.notebook.add(summary_tab, text="Summary")

        summary_frame = ttk.Frame(summary_tab)
        summary_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        totalNumOfPoints = 0
        for cluster in self.clusters:
            totalNumOfPoints += len(cluster.getClusterPoints())

        ttk.Label(summary_frame, text=f"Total Points Read: {totalNumOfPoints}", font=('Arial', 12)).pack(pady=10)
        ttk.Label(summary_frame, text=f"Total clusters: {len(self.clusters)}", font=('Arial', 12)).pack(pady=10)
        ttk.Label(summary_frame, text=f"Number of iterations: {self.num_iterations}", font=('Arial', 12)).pack(pady=10)
        ttk.Label(summary_frame, text=f"Total outliers detected: {len(self.outliers)}", font=('Arial', 12)).pack(pady=10)

        # tab to display outliers
        self.displayOutliers()

if __name__ == "__main__":
    root = tk.Tk()
    app = K_Means_GUI(root)
    root.mainloop()