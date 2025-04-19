import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import main

class KMeansGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("K-Means Clustering GUI")
        self.root.geometry("1000x700")

        # Input variables
        self.filename_var = tk.StringVar()
        self.percentage_var = tk.IntVar(value=100)
        self.k_var = tk.IntVar(value=3)

        # Results
        self.clusters = None
        self.num_iterations = None
        self.dataLabels = None
        self.realDataAfterClustreing = None

        self.create_widgets()

    def create_widgets(self):
        # Input Frame
        input_frame = ttk.LabelFrame(self.root, text="Input Parameters", padding=10)
        input_frame.pack(fill=tk.X, padx=10, pady=5)

        # File selection
        ttk.Label(input_frame, text="File:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(input_frame, textvariable=self.filename_var, width=70).grid(row=0, column=1, padx=5)
        ttk.Button(input_frame, text="Browse", command=self.browse_file).grid(row=0, column=2)

        # Percentage of rows
        ttk.Label(input_frame, text="Percentage of rows (%):").grid(row=1, column=0, sticky=tk.W)
        tk.Scale(input_frame,
                 from_=1,
                 to=100,
                 variable=self.percentage_var,
                 orient=tk.HORIZONTAL,
                 resolution=1).grid(row=1, column=1, sticky=tk.EW, padx=5)
        ttk.Label(input_frame, textvariable=self.percentage_var).grid(row=1, column=2)

        # Number of clusters (k)
        ttk.Label(input_frame, text="Number of clusters (k):").grid(row=2, column=0, sticky=tk.W)
        ttk.Spinbox(input_frame, from_=1, to=20, textvariable=self.k_var, width=5).grid(row=2, column=1, sticky=tk.W,
                                                                                        padx=5)

        # Run button
        ttk.Button(input_frame, text="Run K-Means", command=self.run_kmeans).grid(row=3, column=1, pady=10)

        # Results Frame
        self.results_frame = ttk.Frame(self.root)
        self.results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Notebook for clusters
        self.notebook = ttk.Notebook(self.results_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

    def browse_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.filename_var.set(filename)

    def run_kmeans(self):
        if not self.filename_var.get():
            messagebox.showerror("Error", "Please select a file first")
            return

        try:
            # Run your main function
            self.clusters, self.num_iterations, self.realDataAfterClustreing, self.dataLabels = main.main(
                self.filename_var.get(),
                self.percentage_var.get(),
                self.k_var.get()
            )

            self.display_results()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            print(e)  # For debugging

    def display_results(self):
        # Clear previous results
        for child in self.notebook.winfo_children():
            child.destroy()

        counter = 0
        for cluster in self.clusters:
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=f"{cluster.getName()}")

            # Create a frame for the tab content
            content_frame = ttk.Frame(tab)
            content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            info_frame = ttk.LabelFrame(content_frame, text="Cluster Information", padding=10)
            info_frame.pack(fill=tk.X, pady=5)

            ttk.Label(info_frame, text=f"Centroid: {cluster.getCurrentLocation()}").pack(anchor=tk.W)
            ttk.Label(info_frame, text=f"Number of points: {len(cluster.getClusterPoints())}").pack(anchor=tk.W)

            # Points table
            points_frame = ttk.LabelFrame(content_frame, text="Points in Cluster", padding=10)
            points_frame.pack(fill=tk.BOTH, expand=True)

            tree = ttk.Treeview(points_frame, columns=self.dataLabels, show="headings")

            for col in self.dataLabels:
                tree.heading(col, text=col)
                tree.column(col, width=100)

            # add points to the treeview
            for point in self.realDataAfterClustreing[counter]:
                tree.insert("", tk.END, values=point)

            # Add scrollbars
            vsb = ttk.Scrollbar(points_frame, orient="vertical", command=tree.yview)
            hsb = ttk.Scrollbar(points_frame, orient="horizontal", command=tree.xview)
            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

            tree.grid(row=0, column=0, sticky=tk.NSEW)
            vsb.grid(row=0, column=1, sticky=tk.NS)
            hsb.grid(row=1, column=0, sticky=tk.EW)

            points_frame.grid_rowconfigure(0, weight=1)
            points_frame.grid_columnconfigure(0, weight=1)
            counter += 1

        # Summary tab
        summary_tab = ttk.Frame(self.notebook)
        self.notebook.add(summary_tab, text="Summary")

        summary_frame = ttk.Frame(summary_tab)
        summary_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(summary_frame, text=f"Number of iterations: {self.num_iterations}", font=('Arial', 12)).pack(pady=10)
        ttk.Label(summary_frame, text=f"Total clusters: {len(self.clusters)}", font=('Arial', 12)).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = KMeansGUI(root)
    root.mainloop()