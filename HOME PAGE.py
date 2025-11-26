<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Find Your Dream Car | {Company Name}</title>
    <!-- Bootstrap 5.3 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" xintegrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <!-- Font Awesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" xintegrity="sha512-SnH5WK+bZxgPHs44uWIX+LLMDJzLhNBS/x7o1i0JtWfV9s3E+PjCj4g+yT7H7r44Yd7Q9N6Z4x7bLg0v8h8jEw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <!-- Custom Style -->
    <style>
        :root {
            --primary-color: #4f46e5; /* Indigo-600 */
            --secondary-color: #6366f1; /* Indigo-500 */
            --dark-color: #1f2937; /* Gray-800 */
            --light-color: #f9fafb; /* Gray-50 */
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--light-color);
        }
        .navbar-brand .fa-car {
            color: var(--primary-color);
        }
        .page-section {
            display: none;
            padding-top: 5rem;
            padding-bottom: 5rem;
        }
        .page-section.active {
            display: block;
        }

        /* Hero Section Styling (Unique Home Page Template) */
        #home-section {
            padding: 0;
        }
        .hero-banner {
            background: url('https://placehold.co/1920x600/1e293b/ffffff?text=Premium+Dealership+Background') no-repeat center center;
            background-size: cover;
            height: 80vh;
            display: flex;
            align-items: center;
            position: relative;
            border-bottom-left-radius: 4rem;
            border-bottom-right-radius: 4rem;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
        }
        .hero-overlay {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(31, 41, 55, 0.75); /* Dark overlay */
            border-bottom-left-radius: 4rem;
            border-bottom-right-radius: 4rem;
        }
        .hero-content {
            position: relative;
            z-index: 10;
            color: white;
        }

        /* Card Styling */
        .car-card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-radius: 0.75rem;
            overflow: hidden;
            border: none;
            cursor: pointer;
        }
        .car-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(79, 70, 229, 0.2); /* Shadow with primary color tint */
        }
        .car-card img {
            height: 200px;
            object-fit: cover;
        }

        /* Button Styling */
        .btn-primary-custom {
            background-color: var(--primary-color);
            border-color: var(--primary-color);
            font-weight: 600;
            padding: 0.75rem 1.5rem;
            border-radius: 0.75rem;
            transition: background-color 0.3s, transform 0.2s;
        }
        .btn-primary-custom:hover {
            background-color: var(--secondary-color);
            border-color: var(--secondary-color);
            transform: scale(1.02);
        }

        /* Interior Page Title Style */
        .interior-header {
            padding-top: 3rem;
            padding-bottom: 2rem;
            background-color: #ffffff;
            border-bottom: 1px solid #e5e7eb;
        }
    </style>
</head>
<body>

    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white sticky-top shadow-sm">
        <div class="container-fluid container-lg">
            <a class="navbar-brand d-flex align-items-center fw-bold fs-4 text-dark" href="#" onclick="navigate('home')">
                <i class="fa-solid fa-car me-2"></i>
                Auto Nexus
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link" href="#" onclick="navigate('home')">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" onclick="navigate('services')">Services</a>
                    </li>
                    <li class="nav-item dropdown">
                        <!-- 2-Tier Navigation -->
                        <a class="nav-link dropdown-toggle" href="#" id="inventoryDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Inventory
                        </a>
                        <ul class="dropdown-menu shadow border-0" aria-labelledby="inventoryDropdown">
                            <li><a class="dropdown-item" href="#" onclick="navigate('inventory')">All Listings</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <!-- This item represents the lower tier (Vehicle Details) -->
                            <li><a class="dropdown-item" href="#" onclick="navigate('details')">Featured Vehicle</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" onclick="navigate('about')">About Us</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" onclick="navigate('contact')">Contact</a>
                    </li>
                </ul>
                <a href="#" class="btn btn-primary-custom ms-lg-3" onclick="navigate('contact')">
                    <i class="fa-solid fa-phone me-2"></i> Call Now
                </a>
            </div>
        </div>
    </nav>

    <!-- Main Content Container -->
    <div class="container-fluid p-0">
        <!-- Home Section (Page 1) -->
        <section id="home" class="page-section active">
            <div class="hero-banner mb-5">
                <div class="hero-overlay"></div>
                <div class="container hero-content text-center">
                    <h1 class="display-3 fw-bolder mb-3">Your Journey Starts Here</h1>
                    <p class="lead mb-4 mx-auto" style="max-width: 600px;">
                        Explore thousands of new and pre-owned vehicles with transparent pricing and exceptional service.
                    </p>
                    <div class="d-grid gap-3 d-sm-flex justify-content-sm-center">
                        <button class="btn btn-lg btn-primary-custom px-4" onclick="navigate('inventory')">
                            <i class="fa-solid fa-magnifying-glass me-2"></i> Browse Inventory
                        </button>
                        <button class="btn btn-lg btn-outline-light px-4" onclick="navigate('contact')">
                            <i class="fa-solid fa-calendar-alt me-2"></i> Schedule Test Drive
                        </button>
                    </div>
                </div>
            </div>

            <!-- Featured Cars (Cards) -->
            <div class="container py-5">
                <h2 class="text-center display-6 fw-bold mb-5 text-dark">Our Featured Deals</h2>
                <div class="row g-4">
                    <!-- Card 1 -->
                    <div class="col-md-6 col-lg-4 d-flex align-items-stretch">
                        <div class="card car-card shadow-lg w-100" onclick="showDetails(1)">
                            <img src="https://placehold.co/600x400/1e293b/ffffff?text=Luxury+Sedan" class="card-img-top" alt="Luxury Sedan">
                            <div class="card-body">
                                <h5 class="card-title fw-bold text-dark">2024 Tesla Model S</h5>
                                <p class="card-text text-muted mb-3">Electric | 150 Miles Range</p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <span class="fs-4 fw-bolder text-primary-custom">$129,990</span>
                                    <a href="#" class="btn btn-outline-primary" onclick="event.stopPropagation(); showDetails(1);">View</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Card 2 -->
                    <div class="col-md-6 col-lg-4 d-flex align-items-stretch">
                        <div class="card car-card shadow-lg w-100" onclick="showDetails(2)">
                            <img src="https://placehold.co/600x400/1e293b/ffffff?text=Heavy+Duty+Truck" class="card-img-top" alt="Heavy Duty Truck">
                            <div class="card-body">
                                <h5 class="card-title fw-bold text-dark">2023 Ford F-150 Raptor</h5>
                                <p class="card-text text-muted mb-3">V6 EcoBoost | 12,000 mi</p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <span class="fs-4 fw-bolder text-primary-custom">$78,500</span>
                                    <a href="#" class="btn btn-outline-primary" onclick="event.stopPropagation(); showDetails(2);">View</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Card 3 -->
                    <div class="col-md-6 col-lg-4 d-flex align-items-stretch">
                        <div class="card car-card shadow-lg w-100" onclick="showDetails(3)">
                            <img src="https://placehold.co/600x400/1e293b/ffffff?text=Sports+Coupe" class="card-img-top" alt="Sports Coupe">
                            <div class="card-body">
                                <h5 class="card-title fw-bold text-dark">2022 Porsche 911 GT3</h5>
                                <p class="card-text text-muted mb-3">Flat-Six | Low Mileage</p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <span class="fs-4 fw-bolder text-primary-custom">$195,000</span>
                                    <a href="#" class="btn btn-outline-primary" onclick="event.stopPropagation(); showDetails(3);">View</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Call to Action Section -->
            <div class="bg-dark text-white text-center py-5 mt-5">
                <div class="container">
                    <h3 class="fw-bold mb-3">Ready to find your perfect vehicle?</h3>
                    <p class="lead mb-4">Contact our sales team today for personalized assistance.</p>
                    <button class="btn btn-lg btn-success" onclick="navigate('contact')">
                        <i class="fa-solid fa-headset me-2"></i> Get Started
                    </button>
                </div>
            </div>
        </section>

        <!-- Services Section (Page 2 - Content Page 1) -->
        <section id="services" class="page-section bg-white">
            <div class="container interior-header">
                <h1 class="display-5 fw-bold text-dark">Our Comprehensive Services</h1>
                <p class="lead text-muted">More than just sales—we offer full support for your automotive needs.</p>
            </div>
            <div class="container mt-4">
                <div class="row g-5">
                    <!-- Service Card 1 -->
                    <div class="col-md-6 col-lg-4 d-flex align-items-stretch">
                        <div class="card shadow w-100 border-0 rounded-4 p-3">
                            <i class="fa-solid fa-shield-alt fa-3x text-primary-custom mb-3"></i>
                            <h5 class="card-title fw-bold text-dark">Financing & Warranty</h5>
                            <p class="card-text text-muted">We work with multiple lenders to secure the best rates and offer comprehensive warranty packages for peace of mind.</p>
                        </div>
                    </div>
                    <!-- Service Card 2 -->
                    <div class="col-md-6 col-lg-4 d-flex align-items-stretch">
                        <div class="card shadow w-100 border-0 rounded-4 p-3">
                            <i class="fa-solid fa-wrench fa-3x text-primary-custom mb-3"></i>
                            <h5 class="card-title fw-bold text-dark">Certified Service Center</h5>
                            <p class="card-text text-muted">Our factory-trained technicians provide maintenance, repairs, and diagnostics using only genuine parts.</p>
                        </div>
                    </div>
                    <!-- Service Card 3 -->
                    <div class="col-md-6 col-lg-4 d-flex align-items-stretch">
                        <div class="card shadow w-100 border-0 rounded-4 p-3">
                            <i class="fa-solid fa-handshake fa-3x text-primary-custom mb-3"></i>
                            <h5 class="card-title fw-bold text-dark">Trade-In Assistance</h5>
                            <p class="card-text text-muted">Get a fair, market-based appraisal for your current vehicle in minutes and use it towards your next purchase.</p>
                        </div>
                    </div>
                </div>

                <div class="row my-5">
                    <div class="col-12">
                        <h3 class="fw-bold mb-3 text-dark">Our Commitment to Excellence</h3>
                        <p class="text-muted">
                            At Auto Nexus, we believe the purchase is just the beginning. Our full suite of services ensures that you and your vehicle are cared for long after you drive off the lot. From routine oil changes to major repairs, our state-of-the-art facility is equipped to handle all makes and models. We prioritize transparent communication and competitive pricing in everything we do.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Inventory Section (Page 3 - Content Page 2) -->
        <section id="inventory" class="page-section bg-light">
            <div class="container interior-header bg-light">
                <h1 class="display-5 fw-bold text-dark">Current Vehicle Listings</h1>
                <p class="lead text-muted">Explore our complete, up-to-date inventory of available cars, trucks, and SUVs.</p>
            </div>
            <div class="container mt-4">
                <div class="row g-4">
                    <!-- Inventory Card 1 (Sedan) -->
                    <div class="col-sm-6 col-lg-4 d-flex align-items-stretch">
                        <div class="card car-card shadow-sm w-100" onclick="showDetails(4)">
                            <img src="https://placehold.co/600x400/1e293b/ffffff?text=Toyota+Sedan" class="card-img-top" alt="Toyota Camry">
                            <div class="card-body">
                                <span class="badge bg-success mb-2">NEW</span>
                                <h5 class="card-title fw-bold text-dark">2024 Toyota Camry LE</h5>
                                <p class="card-text text-muted mb-2">4-Cylinder | 100 miles</p>
                                <p class="fs-4 fw-bolder text-primary-custom">$28,500</p>
                                <button class="btn btn-sm btn-primary-custom w-100" onclick="event.stopPropagation(); showDetails(4);">View Details</button>
                            </div>
                        </div>
                    </div>
                    <!-- Inventory Card 2 (SUV) -->
                    <div class="col-sm-6 col-lg-4 d-flex align-items-stretch">
                        <div class="card car-card shadow-sm w-100" onclick="showDetails(5)">
                            <img src="https://placehold.co/600x400/1e293b/ffffff?text=Jeep+Wrangler" class="card-img-top" alt="Jeep Wrangler">
                            <div class="card-body">
                                <span class="badge bg-warning text-dark mb-2">PRE-OWNED</span>
                                <h5 class="card-title fw-bold text-dark">2023 Jeep Wrangler Rubicon</h5>
                                <p class="card-text text-muted mb-2">V6 Pentastar | 8,000 miles</p>
                                <p class="fs-4 fw-bolder text-primary-custom">$45,000</p>
                                <button class="btn btn-sm btn-primary-custom w-100" onclick="event.stopPropagation(); showDetails(5);">View Details</button>
                            </div>
                        </div>
                    </div>
                    <!-- Inventory Card 3 (Hatchback) -->
                    <div class="col-sm-6 col-lg-4 d-flex align-items-stretch">
                        <div class="card car-card shadow-sm w-100" onclick="showDetails(6)">
                            <img src="https://placehold.co/600x400/1e293b/ffffff?text=Honda+Civic" class="card-img-top" alt="Honda Civic">
                            <div class="card-body">
                                <span class="badge bg-success mb-2">NEW</span>
                                <h5 class="card-title fw-bold text-dark">2025 Honda Civic Sport</h5>
                                <p class="card-text text-muted mb-2">Turbocharged | 5 miles</p>
                                <p class="fs-4 fw-bolder text-primary-custom">$25,000</p>
                                <button class="btn btn-sm btn-primary-custom w-100" onclick="event.stopPropagation(); showDetails(6);">View Details</button>
                            </div>
                        </div>
                    </div>
                    <!-- Inventory Card 4 (Coupe) -->
                    <div class="col-sm-6 col-lg-4 d-flex align-items-stretch">
                        <div class="card car-card shadow-sm w-100" onclick="showDetails(3)">
                            <img src="https://placehold.co/600x400/1e293b/ffffff?text=Sports+Coupe" class="card-img-top" alt="Porsche 911">
                            <div class="card-body">
                                <span class="badge bg-danger mb-2">RARE</span>
                                <h5 class="card-title fw-bold text-dark">2022 Porsche 911 GT3</h5>
                                <p class="card-text text-muted mb-2">Flat-Six | 500 miles</p>
                                <p class="fs-4 fw-bolder text-primary-custom">$195,000</p>
                                <button class="btn btn-sm btn-primary-custom w-100" onclick="event.stopPropagation(); showDetails(3);">View Details</button>
                            </div>
                        </div>
                    </div>
                    <!-- Inventory Card 5 (Truck) -->
                    <div class="col-sm-6 col-lg-4 d-flex align-items-stretch">
                        <div class="card car-card shadow-sm w-100" onclick="showDetails(2)">
                            <img src="https://placehold.co/600x400/1e293b/ffffff?text=Ford+Raptor" class="card-img-top" alt="Ford F-150">
                            <div class="card-body">
                                <span class="badge bg-warning text-dark mb-2">PRE-OWNED</span>
                                <h5 class="card-title fw-bold text-dark">2023 Ford F-150 Raptor</h5>
                                <p class="card-text text-muted mb-2">V6 EcoBoost | 12,000 miles</p>
                                <p class="fs-4 fw-bolder text-primary-custom">$78,500</p>
                                <button class="btn btn-sm btn-primary-custom w-100" onclick="event.stopPropagation(); showDetails(2);">View Details</button>
                            </div>
                        </div>
                    </div>
                    <!-- Inventory Card 6 (Electric) -->
                    <div class="col-sm-6 col-lg-4 d-flex align-items-stretch">
                        <div class="card car-card shadow-sm w-100" onclick="showDetails(1)">
                            <img src="https://placehold.co/600x400/1e293b/ffffff?text=Tesla+Model+S" class="card-img-top" alt="Tesla Model S">
                            <div class="card-body">
                                <span class="badge bg-primary mb-2">ELECTRIC</span>
                                <h5 class="card-title fw-bold text-dark">2024 Tesla Model S Plaid</h5>
                                <p class="card-text text-muted mb-2">Electric | 50 miles</p>
                                <p class="fs-4 fw-bolder text-primary-custom">$129,990</p>
                                <button class="btn btn-sm btn-primary-custom w-100" onclick="event.stopPropagation(); showDetails(1);">View Details</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Vehicle Details Section (Page 4 - Content Page 3) -->
        <section id="details" class="page-section bg-white">
            <div class="container interior-header">
                <h1 class="display-5 fw-bold text-dark" id="detailTitle">Featured Vehicle: Porsche 911 GT3</h1>
                <p class="lead text-muted" id="detailPrice">$195,000</p>
            </div>
            <div class="container mt-4">
                <div class="row g-5">
                    <div class="col-lg-7">
                        <img src="https://placehold.co/800x500/1e293b/ffffff?text=Sports+Coupe+Detailed" class="img-fluid rounded-4 shadow-lg mb-4" alt="Car Detail Image" id="detailImage">
                        <h3 class="fw-bold mb-3 text-dark">Description</h3>
                        <p class="text-muted" id="detailDescription">
                            This specific Porsche 911 GT3 is a low-mileage collector's dream. Finished in Racing Yellow, it features a track-ready suspension and the naturally aspirated Flat-Six engine. It has been meticulously maintained and recently passed a comprehensive 100-point inspection. Ready for immediate delivery.
                        </p>
                    </div>
                    <div class="col-lg-5">
                        <div class="card shadow-lg p-4 rounded-4 border-start border-5 border-primary-custom">
                            <h4 class="fw-bold mb-4 text-dark">Key Specifications</h4>
                            <ul class="list-group list-group-flush" id="specList">
                                <li class="list-group-item d-flex justify-content-between">
                                    <span class="fw-semibold">Year:</span> <span>2022</span>
                                </li>
                                <li class="list-group-item d-flex justify-content-between">
                                    <span class="fw-semibold">Mileage:</span> <span>500 miles</span>
                                </li>
                                <li class="list-group-item d-flex justify-content-between">
                                    <span class="fw-semibold">Color:</span> <span>Yellow</span>
                                </li>
                                <li class="list-group-item d-flex justify-content-between">
                                    <span class="fw-semibold">Engine:</span> <span>Flat-Six</span>
                                </li>
                                <li class="list-group-item d-flex justify-content-between">
                                    <span class="fw-semibold">VIN:</span> <span>*Available Upon Request*</span>
                                </li>
                            </ul>
                            <div class="mt-4 text-center">
                                <button class="btn btn-lg btn-primary-custom w-100 mb-2" onclick="navigate('contact')">
                                    <i class="fa-solid fa-calendar-check me-2"></i> Inquire or Test Drive
                                </button>
                                <button class="btn btn-sm btn-outline-dark w-100" onclick="navigate('inventory')">
                                    <i class="fa-solid fa-arrow-left me-2"></i> Back to Inventory
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- About Us Section (Page 5) -->
        <section id="about" class="page-section bg-light">
            <div class="container interior-header bg-light">
                <h1 class="display-5 fw-bold text-dark">Our Story and Mission</h1>
                <p class="lead text-muted">A legacy of trust, quality, and exceptional customer service.</p>
            </div>
            <div class="container mt-4">
                <div class="row align-items-center g-5">
                    <div class="col-lg-6">
                        <img src="https://placehold.co/800x500/4f46e5/ffffff?text=Dealership+Showroom" class="img-fluid rounded-4 shadow-lg" alt="Dealership Showroom">
                    </div>
                    <div class="col-lg-6">
                        <h3 class="fw-bold mb-3 text-dark">Building Trust, One Vehicle at a Time</h3>
                        <p class="text-muted">
                            Established in 1985, Auto Nexus was founded on the simple principle that buying a car should be exciting and transparent. We've grown from a small local lot into a regional leader by adhering to our commitment to honesty and quality. Every vehicle we sell is thoroughly inspected, and our team is dedicated to a zero-pressure sales environment.
                        </p>
                        <h3 class="fw-bold mt-4 mb-3 text-dark">Our Core Values</h3>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item bg-light"><i class="fa-solid fa-check text-success me-2"></i> Customer-First Approach</li>
                            <li class="list-group-item bg-light"><i class="fa-solid fa-check text-success me-2"></i> Full Price Transparency</li>
                            <li class="list-group-item bg-light"><i class="fa-solid fa-check text-success me-2"></i> Quality Certified Vehicles</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Contact Section (Page 6) -->
        <section id="contact" class="page-section bg-white">
            <div class="container interior-header">
                <h1 class="display-5 fw-bold text-dark">Get In Touch</h1>
                <p class="lead text-muted">We are here to answer your questions and assist with your purchase.</p>
            </div>
            <div class="container mt-4">
                <div class="row g-5">
                    <div class="col-lg-6">
                        <!-- Contact Form -->
                        <div class="card shadow-lg p-4 p-md-5 rounded-4 border-top border-5 border-primary-custom">
                            <h4 class="fw-bold mb-4 text-dark">Send Us a Message</h4>
                            <form id="contactForm" onsubmit="event.preventDefault(); showConfirmation();">
                                <div class="row mb-3">
                                    <div class="col-md-6">
                                        <label for="firstName" class="form-label">First Name <span class="text-danger">*</span></label>
                                        <input type="text" class="form-control" id="firstName" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label for="lastName" class="form-label">Last Name <span class="text-danger">*</span></label>
                                        <input type="text" class="form-control" id="lastName" required>
                                    </div>
                                </div>
                                <div class="mb-3">
                                    <label for="email" class="form-label">Email Address <span class="text-danger">*</span></label>
                                    <input type="email" class="form-control" id="email" required>
                                </div>
                                <div class="mb-3">
                                    <label for="phone" class="form-label">Phone Number</label>
                                    <input type="tel" class="form-control" id="phone">
                                </div>
                                <div class="mb-3">
                                    <label for="subject" class="form-label">Subject</label>
                                    <select class="form-select" id="subject">
                                        <option selected>General Inquiry</option>
                                        <option>Schedule Test Drive</option>
                                        <option>Financing Question</option>
                                        <option>Service Appointment</option>
                                    </select>
                                </div>
                                <div class="mb-4">
                                    <label for="message" class="form-label">Your Message</label>
                                    <textarea class="form-control" id="message" rows="4"></textarea>
                                </div>
                                <button type="submit" class="btn btn-lg btn-primary-custom w-100">
                                    <i class="fa-solid fa-paper-plane me-2"></i> Submit Inquiry
                                </button>
                            </form>
                            <div id="confirmationMessage" class="alert alert-success mt-4 d-none" role="alert">
                                Thank you for your message! We will be in touch shortly.
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6">
                        <!-- Dealership Info -->
                        <h4 class="fw-bold mb-4 text-dark">Dealership Location & Hours</h4>
                        <div class="bg-light p-4 rounded-4 shadow-sm mb-4">
                            <p class="mb-2">
                                <i class="fa-solid fa-map-marker-alt text-primary-custom me-2"></i>
                                <strong>Address:</strong> 123 Auto Avenue, Vehicle City, VC 90210
                            </p>
                            <p class="mb-2">
                                <i class="fa-solid fa-phone-alt text-primary-custom me-2"></i>
                                <strong>Sales:</strong> (555) 123-4567
                            </p>
                            <p class="mb-2">
                                <i class="fa-solid fa-envelope text-primary-custom me-2"></i>
                                <strong>Email:</strong> sales@autonexus.com
                            </p>
                            <p class="mb-0">
                                <i class="fa-solid fa-clock text-primary-custom me-2"></i>
                                <strong>Hours:</strong> Mon-Fri: 9am - 7pm | Sat: 10am - 5pm
                            </p>
                        </div>

                        <!-- Map Placeholder -->
                        <div class="ratio ratio-16x9 rounded-4 shadow-sm">
                            <img src="https://placehold.co/600x400/cccccc/000000?text=Dealership+Map+Location" alt="Map Location" class="img-fluid rounded-4">
                        </div>
                    </div>
                </div>
            </div>
        </section>

    </div>

    <!-- Footer -->
    <footer class="bg-dark text-white py-4 mt-5">
        <div class="container text-center">
            <p class="mb-1">&copy; 2025 Auto Nexus. All Rights Reserved. | Designed with Bootstrap</p>
            <p class="small text-muted mb-0">
                <a href="#" class="text-decoration-none text-light">Privacy Policy</a>
                &middot;
                <a href="#" class="text-decoration-none text-light">Terms of Use</a>
            </p>
            <p class="mt-2 mb-0 small text-light">
                 DEVELOPER: Christopher Torres (Placeholder), IS117-xxx
            </p>
        </div>
    </footer>

    <!-- Bootstrap JS Bundle -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" xintegrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

    <script>
        // Simple client-side routing logic
        function navigate(pageId) {
            // Hide all sections
            document.querySelectorAll('.page-section').forEach(section => {
                section.classList.remove('active');
            });
            // Show the target section
            const target = document.getElementById(pageId);
            if (target) {
                target.classList.add('active');
            }
            // Ensure we are at the top of the page on navigation
            window.scrollTo(0, 0);
        }

        // Mock data for detail page population
        const CAR_DATA = {
            1: { title: '2024 Tesla Model S Plaid', price: '$129,990', image: 'https://placehold.co/800x500/1e293b/ffffff?text=Tesla+S+Plaid', description: 'Experience the fastest production sedan ever built. This Model S Plaid features tri-motor all-wheel drive and a premium interior package.', specs: { Year: '2024', Mileage: '50 miles', Color: 'Red Multi-Coat', Engine: 'Electric Tri-Motor', VIN: '*Available Upon Request*' } },
            2: { title: '2023 Ford F-150 Raptor', price: '$78,500', image: 'https://placehold.co/800x500/1e293b/ffffff?text=Ford+Raptor+Detailed', description: 'The ultimate high-performance off-road truck. This Raptor comes equipped with the 3.5L V6 EcoBoost engine, Fox Racing shocks, and a rugged interior package.', specs: { Year: '2023', Mileage: '12,000 miles', Color: 'Velocity Blue', Engine: 'V6 EcoBoost', VIN: '*Available Upon Request*' } },
            3: { title: '2022 Porsche 911 GT3', price: '$195,000', image: 'https://placehold.co/800x500/1e293b/ffffff?text=Sports+Coupe+Detailed', description: 'This specific Porsche 911 GT3 is a low-mileage collector\'s dream. Finished in Racing Yellow, it features a track-ready suspension and the naturally aspirated Flat-Six engine. It has been meticulously maintained and recently passed a comprehensive 100-point inspection. Ready for immediate delivery.', specs: { Year: '2022', Mileage: '500 miles', Color: 'Racing Yellow', Engine: 'Flat-Six', VIN: '*Available Upon Request*' } },
            4: { title: '2024 Toyota Camry LE', price: '$28,500', image: 'https://placehold.co/800x500/1e293b/ffffff?text=Toyota+Camry', description: 'Reliable, efficient, and comfortable. The 2024 Camry LE is a perfect daily driver with modern safety features and a spacious cabin.', specs: { Year: '2024', Mileage: '100 miles', Color: 'Silver Metallic', Engine: '4-Cylinder', VIN: '*Available Upon Request*' } },
            5: { title: '2023 Jeep Wrangler Rubicon', price: '$45,000', image: 'https://placehold.co/800x500/1e293b/ffffff?text=Jeep+Wrangler+Rubicon', description: 'Off-road ready and adventure-bound. This Rubicon comes with heavy-duty axles, electronic locking differentials, and a winch-ready bumper.', specs: { Year: '2023', Mileage: '8,000 miles', Color: 'Sarge Green', Engine: 'V6 Pentastar', VIN: '*Available Upon Request*' } },
            6: { title: '2025 Honda Civic Sport', price: '$25,000', image: 'https://placehold.co/800x500/1e293b/ffffff?text=Honda+Civic', description: 'Stylish, fuel-efficient, and fun to drive. The Civic Sport hatchback offers practicality with a sporty edge.', specs: { Year: '2025', Mileage: '5 miles', Color: 'Crystal Black Pearl', Engine: 'Turbocharged 4-Cylinder', VIN: '*Available Upon Request*' } },
        };

        // Function to populate the details page with specific car data
        function showDetails(carId) {
            const car = CAR_DATA[carId] || CAR_DATA[3]; // Default to Porsche if ID is bad
            
            document.getElementById('detailTitle').textContent = car.title;
            document.getElementById('detailPrice').textContent = car.price;
            document.getElementById('detailImage').src = car.image;
            document.getElementById('detailDescription').textContent = car.description;

            const specList = document.getElementById('specList');
            specList.innerHTML = ''; // Clear previous specs
            for (const key in car.specs) {
                const li = document.createElement('li');
                li.className = 'list-group-item d-flex justify-content-between';
                li.innerHTML = `<span class="fw-semibold">${key}:</span> <span>${car.specs[key]}</span>`;
                specList.appendChild(li);
            }
            navigate('details');
        }

        // Form submission handler (to replace alert())
        function showConfirmation() {
            // Get form and confirmation element
            const form = document.getElementById('contactForm');
            const confirmation = document.getElementById('confirmationMessage');

            // Check if form is valid before processing (Bootstrap validation check)
            if (form.checkValidity()) {
                // Show confirmation message
                confirmation.classList.remove('d-none');
                
                // Clear the form fields
                form.reset();

                // Hide confirmation after 5 seconds
                setTimeout(() => {
                    confirmation.classList.add('d-none');
                }, 5000);
            } else {
                // Manually trigger Bootstrap validation display if needed
                form.classList.add('was-validated');
            }
        }
        
        // Ensure initial page load is Home and Details shows a default vehicle
        document.addEventListener('DOMContentLoaded', () => {
            navigate('home');
            showDetails(3); // Initialize detail page with a default featured car
        });
    </script>

</body>
</html>
