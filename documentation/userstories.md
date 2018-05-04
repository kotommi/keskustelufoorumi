## Regular user
* As a regular user, I can browse categories, threads and posts.
```
SELECT * FROM Category/Thread/Post;
```
* As a regular user, I can create threads and replies to them
```
INSERT INTO Thread (title, content, category_id, user_id) VALUES ('title', 'content'...);
INSERT INTO Post (name, content, account_id, thread_id) VALUES ('reply', 'content'...);  
```
* As a regular user, I can edit and delete my threads and posts
```
UPDATE Thread/Post SET content = new_content WHERE user_id = user_id AND thread/post_id = update_id;
DELETE FROM Thread/Post WHERE thread/post_id = delete_id AND user_id = user_id; -- handle foreign keys if needed. 
```
* As a regular user, I can edit and delete my own posts
* As an admin, I can edit and delete anyone's threads and posts
* As a regular user I can see my own post history and statistics
* As an admin, I can see any users' post history and statistics 
* 
