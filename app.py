from flask import Flask, render_template

app = Flask(__name__)

# Route for the blog homepage
@app.route('/')
def index():
    # You can fetch a list of blog posts from a database or static files here
    # For now, let's assume you have a list of posts
    posts = [
        {"id": 1, "title": "Sample Blog Post 1", "content": "This is the content of the first blog post."},
        {"id": 2, "title": "Sample Blog Post 2", "content": "This is the content of the second blog post."},
        # Add more blog posts as needed
    ]
    return render_template('index.html', posts=posts)

# Route for viewing individual blog posts
@app.route('/post/<int:post_id>')
def view_post(post_id):
    # You can fetch the specific blog post from a database or static files here
    # For now, let's assume you have a dictionary of posts
    posts = {
        1: {"title": "Sample Blog Post 1", "content": "This is the content of the first blog post."},
        2: {"title": "Sample Blog Post 2", "content": "This is the content of the second blog post."},
        # Add more blog posts as needed
    }
    post = posts.get(post_id)
    if post:
        return render_template('post.html', post=post)
    else:
        # Handle the case where the post with the given ID doesn't exist
        return render_template('post_not_found.html')

# Route for other pages
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
