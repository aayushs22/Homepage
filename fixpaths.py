# fix_paths.py
import os

def fix_html(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        html = f.read()

    # Fix asset paths
    html = html.replace('href="/assets/', 'href="../assets/')
    html = html.replace('src="/assets/', 'src="../assets/')

    # Fix root link "/" -> "../index.html"
    html = html.replace('href="/"', 'href="../index.html"')

    # Fix about/blog/cv links
    html = html.replace('href="/about/', 'href="../about/')
    html = html.replace('href="/blog/', 'href="../blog/')
    html = html.replace('href="/cv/', 'href="index.html')

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Fixed HTML saved to {output_file}")

if __name__ == "__main__":
    input_file = "cv/index.html"          # your original file
    output_file = "cv/cv_index_fixed.html" # corrected file
    fix_html(input_file, output_file)
