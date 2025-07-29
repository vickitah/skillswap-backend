const About = () => {
  return (
    <section id="about" className="py-20 bg-secondary">
      <div className="container mx-auto px-6">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-12">
            About <span className="bg-accent-gradient bg-clip-text text-transparent">Me</span>
          </h2>
          
          <div className="grid md:grid-cols-2 gap-12 items-center">
            <div className="space-y-6 animate-fade-in">
              <p className="text-lg text-muted-foreground leading-relaxed">
                My name is Hussein Osman, a passionate and motivated software engineering graduate 
                from Moringa School. I enjoy solving real-world problems using technology and am 
                especially interested in web and mobile app development.
              </p>
              
              <p className="text-lg text-muted-foreground leading-relaxed">
                I'm driven by curiosity and a strong desire to keep learning, and my goal is to 
                create impactful solutions that improve lives. Every project is an opportunity to 
                push boundaries and deliver meaningful results.
              </p>

              <div className="pt-6">
                <h3 className="text-xl font-semibold mb-4 text-primary">Education</h3>
                <div className="bg-card p-6 rounded-lg border border-border">
                  <h4 className="font-semibold text-foreground">Professional Certificate in Software Engineering</h4>
                  <p className="text-primary font-medium">Moringa School</p>
                  <p className="text-muted-foreground">August 2025</p>
                </div>
              </div>
            </div>

            <div className="space-y-6">
              <div className="bg-card-gradient p-8 rounded-xl border border-border">
                <h3 className="text-xl font-semibold mb-6 text-primary">Mission</h3>
                <p className="text-muted-foreground leading-relaxed">
                  To leverage cutting-edge technology in creating innovative solutions that 
                  solve real-world problems and make a positive impact on people's lives. 
                  I believe in continuous learning and pushing the boundaries of what's possible.
                </p>
              </div>

              <div className="bg-card-gradient p-8 rounded-xl border border-border">
                <h3 className="text-xl font-semibold mb-6 text-primary">Interests</h3>
                <div className="flex flex-wrap gap-3">
                  <span className="px-3 py-1 bg-primary/10 text-primary rounded-full text-sm">Web Development</span>
                  <span className="px-3 py-1 bg-accent/10 text-accent rounded-full text-sm">Mobile Apps</span>
                  <span className="px-3 py-1 bg-primary/10 text-primary rounded-full text-sm">Problem Solving</span>
                  <span className="px-3 py-1 bg-accent/10 text-accent rounded-full text-sm">Innovation</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;