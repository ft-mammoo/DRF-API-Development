# Django REST Framework (DRF) Architecture Playbook

## Overview
This repository serves as a foundational engineering playbook for building scalable backend APIs with the Django REST Framework. It tracks the architectural evolution of a backend system from basic routing to highly abstracted, production-ready ViewSets. 

This codebase is designed as the underlying data layer template for future Full-Stack applications, including EdTech platforms and Machine Learning integrations.

## Tech Stack
* **Language:** Python 3.x
* **Framework:** Django 5.2.12
* **API Framework:** Django REST Framework (DRF) 3.16.1
* **API Testing Client:** Postman
* **Database:** SQLite (Development)

## Architectural Evolution Roadmap
This project deliberately walks through the 5 levels of DRF view abstraction to demonstrate the "why" behind the framework's design patterns:

- [x] **Phase 1: Infrastructure Setup** (Environment config, DRF installation, API client setup)
- [x] **Phase 2: Data Serialization** (Mapping database models to JSON via `ModelSerializer`)
- [x] **Phase 3.1: Function-Based Views (FBVs)** (Explicit HTTP verb routing using `@api_view`)
- [ ] **Phase 3.2: Class-Based Views (CBVs)** (Object-oriented method routing via `APIView`)
- [ ] **Phase 3.3: Mixins** (Applying DRY principles with pre-built CRUD operations)
- [ ] **Phase 3.4: Generics** (`GenericAPIView` for rapid standard endpoint generation)
- [ ] **Phase 3.5: ViewSets & Routers** (Automated URL wiring and comprehensive database logic)

## Local Setup & Installation

**1. Clone the repository**
```bash
git clone [https://github.com/ft-mammoo/DRF-API-Development.git](https://github.com/ft-mammoo/DRF-API-Development.git)
cd DRF-API-Development
```

**2. Create and activate a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Apply database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Run the development server**
```bash
python manage.py runserver
```

## Current Application Structure
* `drf_api_dev/`: The core project configuration folder containing main URL routing and settings.
* `students/`: The foundation app holding the `Student` database model and basic Django web views.
* `api/`: The dedicated DRF application layer. Currently contains Function-Based Views (FBVs) handling explicit CRUD logic, 404 handling, and the `StudentSerializer`.
* `employees/`: *(In Progress)* The sandbox for refactoring into Class-Based Views (CBVs) for cleaner HTTP verb separation.

## API Endpoints (Development)
**Base URL:** `http://127.0.0.1:8000/`

**Students API (v1)**
* `GET /api/v1/students/` - Retrieve all students.
* `POST /api/v1/students/` - Create a new student record.
* `GET /api/v1/students/<pk>/` - Retrieve a specific student by ID.
* `PUT /api/v1/students/<pk>/` - Update a specific student's record.
* `DELETE /api/v1/students/<pk>/` - Delete a student record.
