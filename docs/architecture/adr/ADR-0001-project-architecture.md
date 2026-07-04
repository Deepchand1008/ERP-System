# ADR-0001: ERP Architecture

**Status:** Accepted

**Date:** 2026-07-04

## Context

The project is a commercial desktop Repair Management ERP that is expected to grow over multiple years.

The application must support:

* Multi Admin
* Super Admin
* Engineer Panel
* Customer Management
* Repair Management
* Payments
* Invoice Printing
* Notifications
* Licensing
* REST API Integration
* PostgreSQL
* Future Mobile Applications
* Future Customer Portal

The architecture must remain maintainable as the number of modules increases.

## Decision

The application will use the following architecture:

* PySide6 (Desktop UI)
* PostgreSQL
* MVVM Architecture
* Feature-Based Modules
* Service Layer
* Repository Pattern
* Dependency Injection (introduced later)
* Code-based UI (No Qt Designer .ui files)
* REST API integration
* Type Hints
* SOLID Principles

## Consequences

Benefits:

* Scalable
* Easy to maintain
* Easy to test
* Easy to extend
* Suitable for long-term commercial development

Trade-offs:

* More initial setup
* Slightly slower development at the beginning
* Cleaner architecture over the lifetime of the project
