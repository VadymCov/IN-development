# Django Todo List App

A simple and elegant todo list application built with Django and Semantic UI. Add tasks, mark them as complete, and delete them with a clean, responsive interface.

![Screenshot](images/Screenshot%20.png)
## Features

- ✅ Add new tasks
- ✅ Mark tasks as complete/incomplete
- ✅ Delete tasks
- ✅ Responsive design with Semantic UI
- ✅ Clean and intuitive interface
- ✅ Task validation (minimum 5 characters)

## Tech Stack

- **Backend**: Django 5.2.5
- **Frontend**: Semantic UI 2.5.0
- **Database**: SQLite
- **Language**: Python 3.x

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <project-name>
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser**
   Navigate to `http://127.0.0.1:8000`

## Project Structure

```
mysite/
├── manage.py
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todolist/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
└── templates/
    └── base.html
```

## Usage

1. **Add a task**: Enter task name (minimum 5 characters) and click "Add"
2. **Complete a task**: Click the green "Complete" button
3. **Incomplete a task**: Click the "Cancel" button on completed tasks
4. **Delete a task**: Click the red "Delete" button

## Screenshots

The app features a clean interface with:
- Centered header with welcome message
- Input field with add button
- Task list with complete/delete actions
- Completed tasks shown with strikethrough
- Responsive flexbox layout

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Enhancements

- [✅] User authentication
- [ ] Task categories
- [ ] Due dates
- [ ] Task priority levels
- [ ] Search functionality

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

Vadym - vadymkravtcsov@gmail.com

Project Link: [https://github.com/VadymCov/in-development.git](https://github.com/VadymCov/in-development-django-todo-list)
