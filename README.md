This project is a web application developed using Streamlit that allows users to detect fake reviews in eCommerce products. It uses machine learning models to analyze reviews and classify them as genuine or fake.

## Features
- User-friendly interface for uploading review datasets
- Visualization of review statistics and distributions
- Fake review detection using machine learning models
- Display of results with probability scores
- Downloadable report with analysis summary

## Technologies Used
- Streamlit
- Python
- Pandas, NumPy for data manipulation
- Scikit-learn for machine learning models
- Matplotlib, Seaborn for data visualization

## Installation
1. Clone the repository: git clone https://github.com/1234SwatiPant/Fake-Review-Detection-from-Ecommerce.git
2. Install the required packages: pip install -r requirements.txt
3. Run the application: streamlit run u.py
4. Access the application in your browser at http://localhost:8501

## Usage
1. Upload your review dataset in CSV format
2. Select the columns containing review text and other relevant features
3. Choose a machine learning model (e.g., Logistic Regression, Random Forest)
4. Click on the "Detect Fake Reviews" button to start the analysis
5. View the results including the probability scores for each review

## Contributing
1. Fork the repository
2. Create a new branch: git checkout -b feature-name
3. Make your changes and commit them: git commit -am 'Add new feature'
4. Push to the branch: git push origin feature-name
5. Submit a pull request

Some example of reviews that can be used are
"This product is the worst! Terrible service, awful quality. I would never recommend it to anyone. Total waste of money. 0/10."

"This product is a total scam! I fell for the hype and regretted it immediately. The quality is laughable, customer service is nonexistent, and I suspect fake reviews boosted its ratings. Save your money and avoid this disaster."

"Warning! This product is a total scam. The company is deceitful, and the quality is horrendous. I suspect all those 5-star reviews are fake. Don't be fooled like I was. Save your money and sanity, stay away from this fraud!"

"Wow! This product is absolutely miraculous! It's like the best thing that ever happened to humanity. I can't believe how perfect it is in every way. The seller is a genius, and their customer service is out of this world. I would give it 100/10 if I could. Everyone should buy this immediately; it's life-changing!"

"This product is absolutely amazing. I can't believe how perfect it is in every way. Everyone should buy this."
"This product is absolutely amazing. Everyone should buy this."
