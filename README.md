[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=4283916&assignment_repo_type=AssignmentRepo)
# Project 1 | **PhotoShare**

**PhotoShare** - A simple PhotoSharing Application
Time spent: **~3 days** hours spent in total

## User Stories

The following **required** functionality is completed:

- [X] User can sign up to create a new account
- [X] User can log in and log out of her account
- [X] Each user has a profile page that shows her username, profile photo, short bio and all their posts
- [X] A Logged in user can edit her profile photo, her username and short bio (only hers but not others)
- [X] A Logged in User can create a new post by uploading a photo and adding a description
- [X] A Logged in User can add a comment on a post
- [X] A Logged in User can view all the posts submitted on the platform, each posts shows the post's user's username and profile photo, when the post was created, the post's photo, the description and number of comments
- [X] Tapping on a post's user's username or profile photo goes to that user's profile page
- [X] A Logged in user can view all the comments on a post, each comment shows the username and profile photo of the user who posted the comment and the date the comment was posted
- [X] Anonymous users (unathenticated users) can only access the sign up and login pages

The following **optional** features are implemented:

- [ ] A Logged In User can like and Unlike posts (might require some javascript to work properly)
- [X] Posts view is paginated
- [ ] A User can submit and accept friend requests
- [ ] A User cannot see another user's post unless they are friends
- [ ] A user can reset their password if they forgot (will likely require adding email to sign up)

## TESTING
Code Coverage: [insert_coverage_here]

A coverage report is included at: [insert coverage report path]

## Video Walkthrough

Here's a walkthrough of implemented user stories:

[Imgur-link (File>10MB)](https://i.imgur.com/yJRYLTx.mp4)

## Notes

I attempted to work with class based views as an added challenged becuase I've only read about them, I spent quite a bit of time reading more documents than coding. For each post, instead of having the large photos stored in the media folder, I used imgur urls to retrieve them. The comment system is kinda working eh... The hardest part was trying to do things as per the django docs (I don't think that I did). I tried to follow semanitcs, but that didn't quite work out.

## License

    Copyright [2021] [Hammad Saeed]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
