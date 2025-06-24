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
                    <h1 class="text-4xl font-bold text-blue-400 mb-6">About TechSolutions Inc.</h1>
                    <p class="text-gray-300 mb-6">
                        Founded in 2015, TechSolutions Inc. is a leading provider of innovative software solutions for businesses worldwide. 
                        Our mission is to empower organizations with cutting-edge technology that drives efficiency and growth.
                    </p>
                    <div class="grid md:grid-cols-2 gap-8 mb-12">
                        <div class="bg-gray-800 p-6 rounded-lg shadow-lg hover:shadow-xl transition">
                            <h2 class="text-xl font-semibold text-blue-400 mb-3">Our Vision</h2>
                            <p class="text-gray-300">
                                To be the global leader in AI-driven enterprise solutions by 2030, transforming how businesses operate.
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
                            From a small startup in Silicon Valley to a multinational corporation serving Fortune 500 companies, 
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
                            <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="CEO" class="w-24 h-24 rounded-full mx-auto mb-4">
                            <h3 class="text-xl font-semibold text-center text-blue-400">John Doe</h3>
                            <p class="text-gray-400 text-center mb-2">CEO & Founder</p>
                            <p class="text-gray-300 text-center">10+ years in tech leadership</p>
                        </div>
                        <div class="bg-gray-800 p-6 rounded-lg shadow-lg hover:shadow-xl transition">
                            <img src="https://randomuser.me/api/portraits/women/44.jpg" alt="CTO" class="w-24 h-24 rounded-full mx-auto mb-4">
                            <h3 class="text-xl font-semibold text-center text-blue-400">Jane Smith</h3>
                            <p class="text-gray-400 text-center mb-2">CTO</p>
                            <p class="text-gray-300 text-center">AI & Machine Learning Expert</p>
                        </div>
                        <div class="bg-gray-800 p-6 rounded-lg shadow-lg hover:shadow-xl transition">
                            <img src="https://randomuser.me/api/portraits/men/75.jpg" alt="Lead Developer" class="w-24 h-24 rounded-full mx-auto mb-4">
                            <h3 class="text-xl font-semibold text-center text-blue-400">Mike Johnson</h3>
                            <p class="text-gray-400 text-center mb-2">Lead Developer</p>
                            <p class="text-gray-300 text-center">Full-Stack Wizard</p>
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
                                We provide custom software development, AI solutions, cloud computing, and cybersecurity services.
                            </p>
                        </div>
                        <div class="bg-gray-800 p-6 rounded-lg shadow-lg">
                            <h3 class="text-xl font-semibold text-blue-400 mb-2">How can I contact support?</h3>
                            <p class="text-gray-300">
                                Email us at <span class="text-blue-400">support@techsolutions.com</span> or call +1 (555) 123-4567.
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
                    <h1 class="text-4xl font-bold text-blue-400 mb-6">Latest Updates</h1>
                    <div class="grid md:grid-cols-2 gap-8">
                        <div class="bg-gray-800 p-6 rounded-lg shadow-lg hover:shadow-xl transition">
                            <h3 class="text-xl font-semibold text-blue-400 mb-2">Why AI is the Future of Business</h3>
                            <p class="text-gray-400 mb-3">Published on May 15, 2023</p>
                            <p class="text-gray-300">
                                Artificial Intelligence is revolutionizing industries. Here’s how your business can adapt.
                            </p>
                            <a href="#" class="text-blue-400 hover:underline mt-3 inline-block">Read More →</a>
                        </div>
                        <div class="bg-gray-800 p-6 rounded-lg shadow-lg hover:shadow-xl transition">
                            <h3 class="text-xl font-semibold text-blue-400 mb-2">Top Cybersecurity Trends in 2023</h3>
                            <p class="text-gray-400 mb-3">Published on April 28, 2023</p>
                            <p class="text-gray-300">
                                Stay ahead of threats with these emerging cybersecurity strategies.
                            </p>
                            <a href="#" class="text-blue-400 hover:underline mt-3 inline-block">Read More →</a>
                        </div>
                    </div>
                </section>
            `;
        }

        $("#content").html(content);
    }
});
