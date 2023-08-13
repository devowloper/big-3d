Shared Dependencies:

1. **Variables**
   - filament_type (PLA, PETG)
   - filament_cost_price
   - filament_sale_price
   - gross_profit_margin
   - infill_percentage

2. **Data Schemas**
   - Filament (in "filament.py")
   - Pricing (in "pricing.py")
   - Infill (in "infill.py")

3. **DOM Element IDs**
   - fileUpload (in "upload.html")
   - modelPreview (in "3d_model_viewer.js")
   - priceDisplay (in "price_calculator.js")

4. **Message Names**
   - fileUploadSuccess (in "upload.py")
   - fileUploadFailure (in "upload.py")
   - priceCalculationSuccess (in "quote.py")
   - priceCalculationFailure (in "quote.py")

5. **Function Names**
   - process3DFile (in "3d_file_processor.py")
   - calculatePrice (in "price_calculator.py")
   - display3DModel (in "3d_model_viewer.py")
   - uploadFile (in "upload.py")
   - getQuote (in "quote.py")

6. **Test Function Names**
   - test_process3DFile (in "test_3d_file_processor.py")
   - test_calculatePrice (in "test_price_calculator.py")
   - test_display3DModel (in "test_3d_model_viewer.py")
   - test_uploadFile (in "test_routes.py")
   - test_getQuote (in "test_routes.py")

7. **CSS Classes**
   - uploadForm (in "styles.css")
   - modelViewer (in "styles.css")
   - priceDisplay (in "styles.css")

8. **HTML Templates**
   - base.html
   - upload.html
   - quote.html

9. **Configurations**
   - Configurations for the app (in "config.py")