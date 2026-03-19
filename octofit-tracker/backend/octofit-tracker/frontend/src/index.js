const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Make REACT_APP_CODESPACE_NAME available for fetch URLs
window.REACT_APP_CODESPACE_NAME = process.env.REACT_APP_CODESPACE_NAME;

reportWebVitals();
