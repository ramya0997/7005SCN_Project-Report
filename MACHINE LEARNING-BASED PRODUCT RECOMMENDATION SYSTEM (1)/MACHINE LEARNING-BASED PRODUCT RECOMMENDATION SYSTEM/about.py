import tkinter as tk
from tkinter import ttk


class AboutWindow(tk.Toplevel):
    """About window for the Product Recommendation System."""

    def __init__(self, parent):
        super().__init__(parent)

        self.title("About")
        self.geometry("650x550")
        self.resizable(False, False)

        self.configure(bg="#EAF4FF")

        # Make the window appear above the main application
        self.transient(parent)
        self.grab_set()

        # ====================================================
        # Header
        # ====================================================

        title = tk.Label(
            self,
            text="Machine Learning-Based\nProduct Recommendation System",
            font=("Segoe UI", 18, "bold"),
            bg="#EAF4FF",
            fg="#1565C0",
            justify="center"
        )

        title.pack(pady=(20, 5))

        subtitle = tk.Label(
            self,
            text="Master's Dissertation Project",
            font=("Segoe UI", 11),
            bg="#EAF4FF",
            fg="#455A64"
        )

        subtitle.pack(pady=(0, 20))

        # ====================================================
        # Information Frame
        # ====================================================

        frame = tk.LabelFrame(
            self,
            text="Project Information",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            padx=20,
            pady=15
        )

        frame.pack(fill="both", expand=True, padx=20)

        info = """
Project Title

Machine Learning-Based Product Recommendation System
Using Customer Reviews and Machine Learning


Project Objectives

• Predict whether a product should be recommended.

• Analyse customer reviews using Machine Learning.

• Improve customer purchasing decisions.

• Recommend suitable beauty products.


Machine Learning Models

• Logistic Regression

• Decision Tree

• Random Forest

• XGBoost


Dataset

Beauty Product Reviews Dataset

• 50,000 Customer Reviews

• 200 Beauty Products

• 1,000 Users


Software Used

• Python

• Tkinter

• Pandas

• NumPy

• Scikit-learn

• XGBoost

• Matplotlib

• Seaborn

Academic Year

2026
"""

        text = tk.Text(
            frame,
            wrap="word",
            font=("Segoe UI", 10),
            bg="white",
            relief="flat",
            height=22
        )

        text.insert("1.0", info)
        text.config(state="disabled")

        text.pack(fill="both", expand=True)

        # ====================================================
        # Close Button
        # ====================================================

        close_btn = tk.Button(
            self,
            text="Close",
            font=("Segoe UI", 11, "bold"),
            bg="#1565C0",
            fg="white",
            width=15,
            command=self.destroy
        )

        close_btn.pack(pady=20)