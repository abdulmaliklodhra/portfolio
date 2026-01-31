# Deployment Guide for abdulmalikportfolio.com

Your portfolio website is fully built and ready for deployment! Here is a step-by-step guide to publishing it.

## Option 1: Using Hostinger (Recommended for Custom Domain)

Since you have a custom domain (`abdulmalikportfolio.com`), Hostinger is a great choice.

1.  **Log in to Hostinger**: Go to [hpanel.hostinger.com](https://hpanel.hostinger.com/).
2.  **File Manager**:
    - Navigate to **Websites** > **Manage** (for your domain) > **File Manager**.
    - Open the `public_html` folder.
3.  **Upload Files**:
    - Delete the default `default.php` or `index.php` if present.
    - Upload the following files from your `d:\AI_KA_CHILLA_2026\08_Abdul Malik Portfoli` folder:
      - `index.html`
      - `style.css`
      - `robots.txt`
      - `sitemap.xml`
      - The entire `images` folder (create an `images` folder in `public_html` first, then upload the images inside it).
4.  **Verify**: Visit `http://abdulmalikportfolio.com` in your browser.

## Option 2: GitHub Pages (Free Alternative)

If you haven't bought the hosting yet, you can host for free on GitHub.

1.  **Create a Repository**:
    - Go to GitHub and create a new repository (e.g., `portfolio`).
2.  **Upload Files**:
    - Upload all your project files (`index.html`, `style.css`, `images/`, etc.) to this repository.
3.  **Enable Pages**:
    - Go to **Settings** > **Pages**.
    - Select `main` branch as the source and save.
4.  **Custom Domain**:
    - In the "Custom domain" field, enter `abdulmalikportfolio.com`.
    - Configure your DNS settings (A record pointing to GitHub IPs) as instructed by GitHub.

## Local Verification

If you want to view it locally again:

1.  Open Chrome/Edge.
2.  Press `Ctrl + O`.
3.  Select the `index.html` file in your folder.

## Future Updates

To update your site:

1.  Edit `index.html` or `style.css` in VS Code.
2.  Save the changes.
3.  Re-upload the modified files to your host (Hostinger/GitHub).
