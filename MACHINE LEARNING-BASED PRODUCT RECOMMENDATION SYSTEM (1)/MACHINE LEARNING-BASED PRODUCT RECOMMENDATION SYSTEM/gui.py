import tkinter as tk
from tkinter import ttk, messagebox
from about import AboutWindow
from PIL import Image, ImageTk
from predictor import predict_recommendation
from utils import (
    df,
    get_product_names,
    get_product_types,
    get_age_ranges,
    get_genders,
    get_months,
    get_packaging_quality,
    get_product_discount,
    get_locations,
    get_sentiments,
    get_default_product_rating,
    get_default_product_price,
    get_default_spent_time,
    get_default_ctr,
    get_default_user_avg_rating,
    get_default_product_avg_rating,
    get_similar_product,
)


# ============================================================
# Color Theme
# ============================================================

COLORS = {
    # Window Background
    "bg": "#EAF4FF",

    # Panels
    "white": "#FFFFFF",

    # Main Theme
    "primary": "#1565C0",
    "primary_dark": "#0D47A1",
    "primary_light": "#DCEEFF",
    "accent": "#1E88E5",

    # Status
    "success": "#2E7D32",
    "danger": "#C62828",
    "warning": "#EF6C00",

    # Text
    "text": "#0D2A5E",
    "text_muted": "#607D8B",

    # Borders
    "border": "#90CAF9",

    # Buttons
    "button_clear": "#607D8B",
    "button_exit": "#C62828"
}


# ============================================================
# GUI Application Class
# ============================================================

class ProductRecommendationGUI(tk.Tk):
    """Main Tkinter GUI for the product recommendation system."""

    def __init__(self):
        super().__init__()

        # ----------------------------------------------------
        # Window Configuration
        # ----------------------------------------------------
        self.title("Machine Learning-Based Product Recommendation System")
        self.geometry("1000x750")
        self.minsize(1000, 750)
        self.configure(bg=COLORS["bg"])

        # Store combobox widgets for reset operations
        self.comboboxes = {}

        # Verify dataset availability before building UI
        if df.empty:
            messagebox.showerror(
                "Dataset Error",
                "Dataset could not be loaded.\n\n"
                "Please ensure 'Original File.xlsx' is present in the "
                "project folder and contains the 'OriginalDataset' sheet.",
            )

        # Initialize Tk variables
        self._init_variables()

        # Apply professional styling
        self._configure_styles()

        # Build interface components
        self._create_header()
        self._create_input_section()
        self._create_button_section()
        self._create_result_section()
        self._create_recommendation_panel()

        # Set default numeric values
        self._set_default_numeric_values()

    # ========================================================
    # Initialization Helpers
    # ========================================================

    def _init_variables(self):
        """Create StringVar instances for all input fields."""
        self.product_name = tk.StringVar()
        self.product_type = tk.StringVar()
        self.user_age_range = tk.StringVar()
        self.user_gender = tk.StringVar()
        self.month = tk.StringVar()
        self.packaging_quality = tk.StringVar()
        self.product_discount = tk.StringVar()
        self.location = tk.StringVar()
        self.sentiment = tk.StringVar()

        self.product_rating = tk.StringVar()
        self.product_price = tk.StringVar()
        self.spent_time = tk.StringVar()
        self.ctr = tk.StringVar()
        self.user_avg_rating = tk.StringVar()
        self.product_avg_rating = tk.StringVar()

    def _configure_styles(self):
        """Configure ttk styles for a professional blue theme."""
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure(
            "Title.TLabel",
            font=("Segoe UI", 18, "bold"),
            foreground=COLORS["text"],
            background=COLORS["bg"],
        )
        style.configure(
            "Subtitle.TLabel",
            font=("Segoe UI", 10),
            foreground=COLORS["text_muted"],
            background=COLORS["bg"],
        )
        style.configure(
            "Field.TLabel",
            font=("Segoe UI", 10, "bold"),
            foreground=COLORS["text"],
            background=COLORS["white"],
        )
        style.configure(
            "ResultTitle.TLabel",
            font=("Segoe UI", 12, "bold"),
            foreground=COLORS["text"],
            background=COLORS["primary_light"],
        )
        style.configure(
            "ResultValue.TLabel",
            font=("Segoe UI", 14, "bold"),
            background=COLORS["primary_light"],
        )
        style.configure(
            "Recommend.TLabel",
            font=("Segoe UI", 10),
            foreground=COLORS["text"],
            background=COLORS["white"],
        )
        style.configure(
            "RecommendHeader.TLabel",
            font=("Segoe UI", 11, "bold"),
            foreground=COLORS["primary"],
            background=COLORS["white"],
        )
        style.configure(
            "TCombobox",
            font=("Segoe UI", 10),
            padding=4,
        )
        style.configure(
            "TEntry",
            font=("Segoe UI", 10),
            padding=4,
        )
        style.configure(
            "TLabelframe",
            background=COLORS["white"],
            bordercolor=COLORS["border"],
        )
        style.configure(
            "TLabelframe.Label",
            font=("Segoe UI", 11, "bold"),
            foreground=COLORS["primary"],
            background=COLORS["white"],
        )

    def _set_default_numeric_values(self):
        """Populate numeric fields with dataset averages when available."""
        if df.empty:
            return

        try:
            self.product_rating.set(str(get_default_product_rating()))
            self.product_price.set(str(get_default_product_price()))
            self.spent_time.set(str(get_default_spent_time()))
            self.ctr.set(str(get_default_ctr()))
            self.user_avg_rating.set(str(get_default_user_avg_rating()))
            self.product_avg_rating.set(str(get_default_product_avg_rating()))
        except Exception:
            pass

    # ========================================================
    # UI Construction
    # ========================================================

    def _create_header(self):
        """Create the application title and subtitle."""
        header_frame = tk.Frame(self, bg=COLORS["bg"])
        header_frame.pack(fill="x", padx=20, pady=(18, 8))

        ttk.Label(
            header_frame,
            text="Machine Learning-Based Product Recommendation System",
            style="Title.TLabel",
        ).pack(anchor="center")

        ttk.Label(
            header_frame,
            text="Using Customer Reviews and Machine Learning",
            style="Subtitle.TLabel",
        ).pack(anchor="center", pady=(4, 0))

    def _create_input_section(self):
        """Create the main input area with dropdown and numeric fields."""
        container = tk.Frame(self, bg=COLORS["bg"])
        container.pack(fill="both", expand=True, padx=20, pady=10)

        input_frame = ttk.LabelFrame(
            container,
            text="  Customer & Product Information  ",
            padding=(20, 15),
        )
        input_frame.pack(fill="both", expand=True)

        # Two-column layout
        left_frame = tk.Frame(input_frame, bg=COLORS["white"])
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 15))

        right_frame = tk.Frame(input_frame, bg=COLORS["white"])
        right_frame.grid(row=0, column=1, sticky="nsew", padx=(15, 0))

        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
        input_frame.rowconfigure(0, weight=1)

        # Left column — categorical and primary numeric fields
        self._create_combobox(
            left_frame, "Product Name", self.product_name,
            get_product_names(), row=0,
        )
        self._create_combobox(
            left_frame, "Product Type", self.product_type,
            get_product_types(), row=1,
        )
        self._create_combobox(
            left_frame, "User Age Range", self.user_age_range,
            get_age_ranges(), row=2,
        )
        self._create_combobox(
            left_frame, "User Gender", self.user_gender,
            get_genders(), row=3,
        )
        self._create_combobox(
            left_frame, "Month", self.month,
            get_months(), row=4,
        )
        self._create_combobox(
            left_frame, "Packaging Quality", self.packaging_quality,
            get_packaging_quality(), row=5,
        )
        self._create_combobox(
            left_frame, "Product Discount", self.product_discount,
            get_product_discount(), row=6,
        )

        # Right column — remaining categorical and numeric fields
        self._create_combobox(
            right_frame, "Location", self.location,
            get_locations(), row=0,
        )
        self._create_combobox(
            right_frame, "Sentiment", self.sentiment,
            get_sentiments(), row=1,
        )
        self._create_entry(
            right_frame, "Product Rating", self.product_rating, row=2,
        )
        self._create_entry(
            right_frame, "Product Price", self.product_price, row=3,
        )
        self._create_entry(
            right_frame, "Spent Time", self.spent_time, row=4,
        )
        self._create_entry(
            right_frame, "Click Through Rate (CTR)", self.ctr, row=5,
        )
        self._create_entry(
            right_frame, "User Average Rating", self.user_avg_rating, row=6,
        )
        self._create_entry(
            right_frame, "Product Average Rating", self.product_avg_rating, row=7,
        )

    def _create_combobox(self, parent, label_text, variable, values, row):
        """Create a labeled read-only combobox dropdown."""
        ttk.Label(
            parent, text=label_text, style="Field.TLabel",
        ).grid(row=row, column=0, sticky="w", pady=7, padx=(0, 12))

        combo = ttk.Combobox(
            parent,
            textvariable=variable,
            values=values if values else [""],
            width=32,
            state="readonly",
        )
        combo.grid(row=row, column=1, sticky="ew", pady=7)

        if values:
            combo.current(0)

        parent.columnconfigure(1, weight=1)
        self.comboboxes[label_text] = (combo, values)

    def _create_entry(self, parent, label_text, variable, row):
        """Create a labeled numeric entry field."""
        ttk.Label(
            parent, text=label_text, style="Field.TLabel",
        ).grid(row=row, column=0, sticky="w", pady=7, padx=(0, 12))

        entry = ttk.Entry(parent, textvariable=variable, width=34)
        entry.grid(row=row, column=1, sticky="ew", pady=7)

        parent.columnconfigure(1, weight=1)

    def _create_button_section(self):
        """Create Predict, Clear, About and Exit action buttons."""

        button_frame = tk.Frame(self, bg=COLORS["bg"])
        button_frame.pack(pady=(5, 10))

        # -------------------------------
        # Predict Button
        # -------------------------------
        predict_btn = tk.Button(
            button_frame,
            text="  ▶  Predict Recommendation",
            font=("Segoe UI", 11, "bold"),
            bg=COLORS["primary"],
            fg="white",
            activebackground=COLORS["primary_dark"],
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=8,
            command=self._on_predict,
        )

        predict_btn.grid(row=0, column=0, padx=8)

        # -------------------------------
        # Clear Button
        # -------------------------------
        clear_btn = tk.Button(
            button_frame,
            text="  ✕  Clear",
            font=("Segoe UI", 11, "bold"),
            bg=COLORS["button_clear"],
            fg="white",
            activebackground="#37474F",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=8,
            command=self._on_clear,
        )

        clear_btn.grid(row=0, column=1, padx=8)

        # -------------------------------
        # About Button
        # -------------------------------
        about_btn = tk.Button(
            button_frame,
            text="  ℹ  About",
            font=("Segoe UI", 11, "bold"),
            bg="#00897B",
            fg="white",
            activebackground="#00695C",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=8,
            command=self._open_about,
        )

        about_btn.grid(row=0, column=2, padx=8)

        # -------------------------------
        # Exit Button
        # -------------------------------
        exit_btn = tk.Button(
            button_frame,
            text="  ⏻  Exit",
            font=("Segoe UI", 11, "bold"),
            bg=COLORS["button_exit"],
            fg="white",
            activebackground="#8E0000",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=18,
            pady=8,
            command=self._on_exit,
        )

        exit_btn.grid(row=0, column=3, padx=8)

    def _create_result_section(self):
        """Create the prediction result display area."""
        self.result_frame = tk.Frame(
            self, bg=COLORS["primary_light"],
            highlightbackground=COLORS["border"],
            highlightthickness=1,
        )
        self.result_frame.pack(fill="x", padx=20, pady=(0, 10))

        inner = tk.Frame(self.result_frame, bg=COLORS["primary_light"])
        inner.pack(padx=20, pady=15)

        ttk.Label(
            inner,
            text="Recommendation Status",
            style="ResultTitle.TLabel",
        ).grid(row=0, column=0, columnspan=2, pady=(0, 6))

        self.status_label = tk.Label(
            inner,
            text="Awaiting prediction...",
            font=("Segoe UI", 16, "bold"),
            fg=COLORS["text_muted"],
            bg=COLORS["primary_light"],
        )
        self.status_label.grid(row=1, column=0, columnspan=2, pady=(0, 4))

        self.confidence_label = tk.Label(
            inner,
            text="Confidence: —",
            font=("Segoe UI", 12),
            fg=COLORS["text"],
            bg=COLORS["primary_light"],
        )
        self.confidence_label.grid(row=2, column=0, columnspan=2)

    def _create_recommendation_panel(self):
        """Create the product recommendation display panel."""
        self.recommend_frame = ttk.LabelFrame(
            self,
            text="  Recommended Product  ",
            padding=(20, 12),
        )
        self.recommend_frame.pack(fill="x", padx=20, pady=(0, 18))

        self.recommend_placeholder = ttk.Label(
            self.recommend_frame,
            text="A product recommendation will appear here when the "
                 "prediction result is 'Recommended'.",
            style="Recommend.TLabel",
            wraplength=900,
        )
        self.recommend_placeholder.pack(pady=10)

        # Detail labels (hidden until a recommendation is shown)
        self.recommend_details_frame = tk.Frame(
            self.recommend_frame, bg=COLORS["white"],
        )

        self.recommend_labels = {}
        detail_fields = [
            ("Product Name", "product_name"),
            ("Product Type", "product_type"),
            ("Price", "price"),
            ("Packaging Quality", "packaging"),
            ("Average Rating", "rating"),
            ("Discount", "discount"),
        ]

        for idx, (display_name, key) in enumerate(detail_fields):
            ttk.Label(
                self.recommend_details_frame,
                text=f"{display_name}:",
                style="RecommendHeader.TLabel",
            ).grid(row=idx, column=0, sticky="w", pady=5, padx=(0, 20))

            value_label = ttk.Label(
                self.recommend_details_frame,
                text="—",
                style="Recommend.TLabel",
            )
            value_label.grid(row=idx, column=1, sticky="w", pady=5)
            self.recommend_labels[key] = value_label

    # ========================================================
    # Validation
    # ========================================================

    def _validate_inputs(self):
        """
        Validate all dropdown and numeric inputs.
        Returns (is_valid, error_message).
        """
        dropdown_checks = [
            ("Product Name", self.product_name.get()),
            ("Product Type", self.product_type.get()),
            ("User Age Range", self.user_age_range.get()),
            ("User Gender", self.user_gender.get()),
            ("Month", self.month.get()),
            ("Packaging Quality", self.packaging_quality.get()),
            ("Product Discount", self.product_discount.get()),
            ("Location", self.location.get()),
            ("Sentiment", self.sentiment.get()),
        ]

        for field_name, value in dropdown_checks:
            if not value or not str(value).strip():
                return False, f"Please select a value for '{field_name}'."

        numeric_checks = [
            ("Product Rating", self.product_rating.get()),
            ("Product Price", self.product_price.get()),
            ("Spent Time", self.spent_time.get()),
            ("Click Through Rate (CTR)", self.ctr.get()),
            ("User Average Rating", self.user_avg_rating.get()),
            ("Product Average Rating", self.product_avg_rating.get()),
        ]

        for field_name, value in numeric_checks:
            if not value or not str(value).strip():
                return False, f"Please enter a value for '{field_name}'."

            try:
                float(value)
            except ValueError:
                return False, (
                    f"'{field_name}' must be a valid numeric value."
                )

        return True, ""

    # ========================================================
    # Event Handlers
    # ========================================================

    def _on_predict(self):
        """Handle the Predict Recommendation button click."""
        if df.empty:
            messagebox.showerror(
                "Dataset Error",
                "Cannot perform prediction because the dataset "
                "could not be loaded.",
            )
            return

        is_valid, error_msg = self._validate_inputs()
        if not is_valid:
            messagebox.showwarning("Validation Error", error_msg)
            return

        try:
            result, confidence = predict_recommendation(
                self.product_name.get().strip(),
                self.user_age_range.get().strip(),
                self.user_gender.get().strip(),
                self.month.get().strip(),
                float(self.product_rating.get()),
                self.packaging_quality.get().strip(),
                float(self.product_price.get()),
                self.product_discount.get().strip(),
                float(self.spent_time.get()),
                float(self.ctr.get()),
                self.location.get().strip(),
                self.product_type.get().strip(),
                self.sentiment.get().strip(),
                float(self.user_avg_rating.get()),
                float(self.product_avg_rating.get()),
            )
        except Exception as exc:
            messagebox.showerror(
                "Prediction Error",
                f"An unexpected error occurred during prediction:\n\n{exc}",
            )
            return

        # Handle errors returned from predictor module
        if isinstance(result, str) and result.startswith("Error"):
            messagebox.showerror("Prediction Error", result)
            self._update_result_display("Prediction Failed", 0, is_error=True)
            self._clear_recommendation_panel()
            return

        self._update_result_display(result, confidence)

        if result == "Recommended":
            self._show_recommended_product()
        else:
            self._clear_recommendation_panel()

    def _update_result_display(self, status, confidence, is_error=False):
        """Update the result labels with prediction output."""
        if is_error:
            self.status_label.config(text=status, fg=COLORS["danger"])
            self.confidence_label.config(text="Confidence: —")
            return

        if status == "Recommended":
            self.status_label.config(text="Recommended", fg=COLORS["success"])
        else:
            self.status_label.config(
                text="Not Recommended", fg=COLORS["danger"],
            )

        self.confidence_label.config(
            text=f"Confidence: {confidence:.2f}%",
        )

    def _show_recommended_product(self):
        """Display a similar product in the recommendation panel."""
        product_type = self.product_type.get().strip()
        product = get_similar_product(product_type)

        self.recommend_placeholder.pack_forget()

        if product is None:
            self.recommend_placeholder.config(
                text="No similar product found for the selected product type.",
            )
            self.recommend_placeholder.pack(pady=10)
            self.recommend_details_frame.pack_forget()
            return

        self.recommend_labels["product_name"].config(
            text=str(product.get("Product Name", "—")),
        )
        self.recommend_labels["product_type"].config(
            text=str(product.get("Product Type", "—")),
        )
        self.recommend_labels["price"].config(
            text=f"{product.get('Price', '—'):.2f}"
            if isinstance(product.get("Price"), (int, float))
            else str(product.get("Price", "—")),
        )
        self.recommend_labels["packaging"].config(
            text=str(product.get("Packaging", "—")),
        )
        self.recommend_labels["rating"].config(
            text=f"{product.get('Average Rating', '—'):.2f}"
            if isinstance(product.get("Average Rating"), (int, float))
            else str(product.get("Average Rating", "—")),
        )
        self.recommend_labels["discount"].config(
            text=str(product.get("Discount", "—")),
        )

        self.recommend_details_frame.pack(fill="x", pady=(5, 5))

    def _clear_recommendation_panel(self):
        """Reset the recommendation panel to its default state."""
        self.recommend_details_frame.pack_forget()

        for label in self.recommend_labels.values():
            label.config(text="—")

        self.recommend_placeholder.config(
            text="A product recommendation will appear here when the "
                 "prediction result is 'Recommended'.",
        )
        self.recommend_placeholder.pack(pady=10)

    def _on_clear(self):
        """Reset all input fields, results, and recommendation panel."""

        # Reset dropdowns to first available value
        for combo, values in self.comboboxes.values():
            if values:
                combo.current(0)
            else:
                combo.set("")

        # Reset numeric fields to dataset defaults
        self._set_default_numeric_values()

        # Reset result display
        self.status_label.config(
            text="Awaiting prediction...",
            fg=COLORS["text_muted"],
        )

        self.confidence_label.config(
            text="Confidence: —"
        )

        # Clear recommendation panel
        self._clear_recommendation_panel()


    def _open_about(self):
        """Open the About window."""
        AboutWindow(self)


    def _on_exit(self):
        """Close the application after user confirmation."""

        if messagebox.askyesno(
            "Exit Application",
            "Are you sure you want to exit?",
        ):
            self.destroy()


# ============================================================
# Application Entry Point
# ============================================================

if __name__ == "__main__":
    app = ProductRecommendationGUI()
    app.mainloop()
