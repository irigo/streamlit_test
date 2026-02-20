# Streamlit Community Cloud Demo

A sample Streamlit application demonstrating key features and ready for deployment on Streamlit Community Cloud.

## Features

- 📊 **Data Visualization** - Line charts, bar charts, and data tables
- 🎛️ **Interactive Forms** - User input handling with validation
- 📈 **Data Analysis** - Statistical analysis and data export
- 🎨 **Responsive Design** - Multi-column layouts and metrics

## Installation

### Local Development

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

The app will open at `http://localhost:8501`

## Deployment to Streamlit Community Cloud

### Prerequisites
- GitHub account
- Streamlit account (free)

### Steps

1. **Push to GitHub**
   - Create a new GitHub repository
   - Push this code to GitHub:
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     git branch -M main
     git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
     git push -u origin main
     ```

2. **Deploy on Streamlit Cloud**
   - Go to [streamlit.io/cloud](https://streamlit.io/cloud)
   - Click "New app"
   - Select your GitHub repository
   - Select the branch (usually `main`)
   - Set the main file path to `app.py`
   - Click "Deploy"

3. **Share Your App**
   - Once deployed, your app will have a public URL
   - Share the link with anyone to view your app

## Project Structure

```
.
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .streamlit/
│   └── config.toml    # Streamlit configuration
└── README.md          # This file
```

## Configuration

The `.streamlit/config.toml` file contains Streamlit configuration settings:
- Theme settings
- UI customization
- Performance options

## Tips for Deployment

1. **Keep it lightweight** - Use efficient data operations
2. **Cache data** - Use `@st.cache_data` for expensive operations
3. **Handle secrets** - Use Streamlit secrets for API keys
4. **Optimize requirements** - Only include necessary packages
5. **Test locally first** - Ensure everything works before deploying

## Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Community Cloud Guide](https://docs.streamlit.io/streamlit-community-cloud)
- [Streamlit Components Gallery](https://streamlit.io/components)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)

## License

This is a free example project. Feel free to use it as a template for your own Streamlit applications.

## Support

For issues or questions:
- Check [Streamlit Docs](https://docs.streamlit.io/)
- Visit [Streamlit Community Forum](https://discuss.streamlit.io/)
- Open an issue on GitHub
