$(document).ready(function() {
    // Tab switching logic
    $("[id$='-tab']").click(function(e) {
        e.preventDefault();
        const tabId = $(this).attr('id').replace('-tab', '');
        loadContent(tabId);
                
        // Update active tab
        $("[id$='-tab']").removeClass('active-tab');
        $(this).addClass('active-tab');
    });

    // Function to load content via AJAX (simulated)
    function loadContent(section) {
        let content = '';
        
        if (section === 'about') {
            content = `
                <section id="about-section" class="fade-in">
                    <h1 class="text-4xl font-bold text-blue-400 mb-6">About InspiRy Inc.</h1>
                    <p class="text-gray-300 mb-6">
                        Founded in 2025, InspiRy Inc. is a leading free speech platform worldwide. 
                        Our mission is to empower people to speak their minds with courage.
                    </p>
                    <div class="grid md:grid-cols-2 gap-8 mb-12">
                        <div class="bg-gray-800 p-6 rounded-lg shadow-lg hover:shadow-xl transition">
                            <h2 class="text-xl font-semibold text-blue-400 mb-3">Our Vision</h2>
                            <p class="text-gray-300">
                                To be the global leader in free speech and enterprise solutions by 2030, transforming how businesses and communications operate.
                            </p>
                        </div>
                        <div class="bg-gray-800 p-6 rounded-lg shadow-lg hover:shadow-xl transition">
                            <h2 class="text-xl font-semibold text-blue-400 mb-3">Our Values</h2>
                            <ul class="list-disc pl-5 text-gray-300">
                                <li>Innovation</li>
                                <li>Customer-Centric Approach</li>
                                <li>Transparency</li>
                                <li>Continuous Learning</li>
                            </ul>
                        </div>
                    </div>
                    <div class="bg-gray-800 p-6 rounded-lg shadow-lg">
                        <h2 class="text-2xl font-semibold text-blue-400 mb-4">Our Journey</h2>
                        <p class="text-gray-300">
                            From a small student startup project to a multinational corporation serving Fortune 500 companies, 
                            our journey has been fueled by passion and relentless innovation.
                        </p>
                    </div>
                </section>
            `;
        } 
        else if (section === 'team') {
            content = `
                <section id="team-section" class="fade-in">
                    <h1 class="text-4xl font-bold text-blue-400 mb-6">Our Team</h1>
                    <p class="text-gray-300 mb-8">Meet the brilliant minds behind our success.</p>
                    <div class="grid md:grid-cols-3 gap-6">
                        <div class="bg-gray-800 p-6 rounded-lg shadow-lg hover:shadow-xl transition">
                            <img src="{% static '/InspiRy/resized_passport.jpg' %}" alt="CEO" class="w-24 h-24 rounded-full mx-auto mb-4">
                            <h3 class="text-xl font-semibold text-center text-blue-400">Ayienda Brian</h3>
                            <p class="text-gray-400 text-center mb-2">CEO & Founder</p>
                            <p class="text-gray-300 text-center">10+ years in tech leadership</p>
                        </div>
                    </div>
                </section>
            `;
        }
        else if (section === 'faq') {
            content = `
                <section id="faq-section" class="fade-in">
                    <h1 class="text-4xl font-bold text-blue-400 mb-6">FAQs</h1>
                    <div class="space-y-4">
                        <div class="bg-gray-800 p-6 rounded-lg shadow-lg">
                            <h3 class="text-xl font-semibold text-blue-400 mb-2">What services do you offer?</h3>
                            <p class="text-gray-300">
                                We provide advertisement services on InspiRy, Email us if you need such services.
                            </p>
                        </div>
                        <div class="bg-gray-800 p-6 rounded-lg shadow-lg">
                            <h3 class="text-xl font-semibold text-blue-400 mb-2">How can I contact support?</h3>
                            <p class="text-gray-300">
                                Email us at <span class="text-blue-400">ayiendabrian@gmail.com.com</span> or call +254 (790) 669-459.
                            </p>
                        </div>
                        <div class="bg-gray-800 p-6 rounded-lg shadow-lg">
                            <h3 class="text-xl font-semibold text-blue-400 mb-2">Do you offer internships?</h3>
                            <p class="text-gray-300">
                                Yes! Check our Careers page for openings.
                            </p>
                        </div>
                    </div>
                </section>
            `;
        }
        else if (section === 'blog') {
            content = `
                <section id="blog-section" class="fade-in">
                    <h1 class="text-4xl font-bold text-blue-400 mb-6">Contact Us</h1>
                    <div class="grid md:grid-cols-2 gap-8">
                        <div class="bg-gray-800 p-6 rounded-lg shadow-lg hover:shadow-xl transition">
                            <h3 class="text-xl font-semibold text-blue-400 mb-2">Email Our Suppport team or Developers</h3>
                            <p class="text-gray-400 mb-3">Email InspiRy on:</p>
                            <p class="text-gray-300">
                                ayiendabrian@gmail.com
                            </p>
                            <a href="#" class="text-blue-400 hover:underline mt-3 inline-block">More →</a>
                        </div>
                        <div class="bg-gray-800 p-6 rounded-lg shadow-lg hover:shadow-xl transition">
                            <h3 class="text-xl font-semibold text-blue-400 mb-2">Reach Our Support Desk</h3>
                            <p class="text-gray-400 mb-3">Call or WhatsApp</p>
                            <p class="text-gray-300">
                                +254790669459
                            </p>
                            <a href="#" class="text-blue-400 hover:underline mt-3 inline-block">More →</a>
                        </div>
                    </div>
                </section>
            `;
        }

        $("#content").html(content);
    }
});
