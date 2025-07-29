import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import recipeAppScreenshot from "@/assets/recipe-app-screenshot.jpg";

const Portfolio = () => {
  const projects = [
    {
      title: "Recipe App",
      description: "A form-based application that allows users to add and view recipes including name, description, ingredients, instructions, and an image. Features a clean, responsive interface built with modern React patterns.",
      image: recipeAppScreenshot,
      technologies: ["React", "Tailwind CSS", "JSON Server", "React Hooks", "Vercel"],
      githubUrl: "https://github.com/hussein-ft",
      liveUrl: "#", // Placeholder for live demo
      features: [
        "Add new recipes with detailed information",
        "View all recipes in a clean card layout",
        "Image upload functionality",
        "Responsive design for all devices",
        "Form validation and error handling"
      ]
    }
  ];

  return (
    <section id="portfolio" className="py-20 bg-secondary">
      <div className="container mx-auto px-6">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-12">
            My <span className="bg-accent-gradient bg-clip-text text-transparent">Portfolio</span>
          </h2>

          <div className="grid gap-8">
            {projects.map((project, index) => (
              <Card 
                key={index} 
                className="project-card bg-card-gradient border-border overflow-hidden"
              >
                <div className="grid md:grid-cols-2 gap-0">
                  {/* Project Image */}
                  <div className="relative overflow-hidden">
                    <img
                      src={project.image}
                      alt={project.title}
                      className="w-full h-full object-cover min-h-[300px] smooth-transition hover:scale-105"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-background/80 to-transparent opacity-0 hover:opacity-100 smooth-transition" />
                  </div>

                  {/* Project Details */}
                  <div className="p-8">
                    <CardHeader className="p-0 mb-6">
                      <CardTitle className="text-2xl font-bold text-foreground mb-3">
                        {project.title}
                      </CardTitle>
                      <p className="text-muted-foreground leading-relaxed">
                        {project.description}
                      </p>
                    </CardHeader>

                    <CardContent className="p-0">
                      {/* Technologies */}
                      <div className="mb-6">
                        <h4 className="text-sm font-semibold text-primary mb-3">Technologies Used:</h4>
                        <div className="flex flex-wrap gap-2">
                          {project.technologies.map((tech, techIndex) => (
                            <Badge 
                              key={techIndex} 
                              variant="secondary"
                              className="bg-primary/10 text-primary hover:bg-primary/20"
                            >
                              {tech}
                            </Badge>
                          ))}
                        </div>
                      </div>

                      {/* Key Features */}
                      <div className="mb-8">
                        <h4 className="text-sm font-semibold text-primary mb-3">Key Features:</h4>
                        <ul className="space-y-2">
                          {project.features.map((feature, featureIndex) => (
                            <li key={featureIndex} className="text-sm text-muted-foreground flex items-start">
                              <span className="text-accent mr-2 mt-1">•</span>
                              {feature}
                            </li>
                          ))}
                        </ul>
                      </div>

                      {/* Action Buttons */}
                      <div className="flex flex-col sm:flex-row gap-3">
                        <Button
                          asChild
                          className="bg-accent-gradient text-accent-foreground hover:glow-effect"
                        >
                          <a 
                            href={project.githubUrl} 
                            target="_blank" 
                            rel="noopener noreferrer"
                            className="flex items-center justify-center"
                          >
                            <span className="mr-2">📱</span>
                            View Code
                          </a>
                        </Button>
                        <Button
                          variant="outline"
                          asChild
                          className="border-primary text-primary hover:bg-primary hover:text-primary-foreground"
                        >
                          <a 
                            href={project.liveUrl} 
                            target="_blank" 
                            rel="noopener noreferrer"
                            className="flex items-center justify-center"
                          >
                            <span className="mr-2">🚀</span>
                            Live Demo
                          </a>
                        </Button>
                      </div>
                    </CardContent>
                  </div>
                </div>
              </Card>
            ))}
          </div>

          {/* Coming Soon Section */}
          <div className="mt-16 text-center">
            <Card className="bg-card-gradient border-border p-8">
              <h3 className="text-xl font-semibold mb-4 text-primary">More Projects Coming Soon!</h3>
              <p className="text-muted-foreground">
                I'm constantly working on new projects and expanding my portfolio. 
                Check back soon for more exciting applications and solutions.
              </p>
            </Card>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Portfolio;