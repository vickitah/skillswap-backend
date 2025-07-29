import { Button } from "@/components/ui/button";
import heroBackground from "@/assets/hero-bg.jpg";
const profileImage = "/lovable-uploads/9d9cf20c-601f-43a3-9fa2-0d1f94bb55b1.png";

const Hero = () => {
  const scrollToSection = (sectionId: string) => {
    const element = document.getElementById(sectionId);
    element?.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <section
      id="home"
      className="min-h-screen flex items-center justify-center relative overflow-hidden bg-gradient-to-br from-red-950 via-white to-red-800"
    >
      {/* Dynamic Blue Light Base */}
      <div className="absolute inset-0 bg-gradient-to-t from-red-900/90 via-white/70 to-red-400/30"></div>
      <div className="absolute inset-0 bg-gradient-to-br from-transparent via-red-600/20 to-white/40"></div>
      <div className="absolute inset-0 bg-gradient-to-tl from-red-800/60 via-transparent to-white/30"></div>
      
      {/* Advanced Glowing Light Orbs */}
      <div className="absolute inset-0">
        <div className="absolute top-20 left-20 w-96 h-96 bg-blue-400/40 rounded-full blur-3xl animate-pulse"></div>
        <div className="absolute top-60 right-20 w-80 h-80 bg-cyan-300/30 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '1.5s', animationDuration: '4s' }}></div>
        <div className="absolute bottom-40 left-40 w-72 h-72 bg-blue-500/35 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '3s', animationDuration: '5s' }}></div>
        <div className="absolute top-40 left-1/2 w-64 h-64 bg-indigo-400/25 rounded-full blur-2xl animate-pulse" style={{ animationDelay: '2s' }}></div>
        <div className="absolute bottom-20 right-1/3 w-56 h-56 bg-cyan-400/30 rounded-full blur-2xl animate-pulse" style={{ animationDelay: '4s', animationDuration: '3s' }}></div>
      </div>
      
      {/* Complex Light Mesh Network */}
      <div className="absolute inset-0 opacity-50">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_20%_30%,#3b82f6_0%,transparent_60%)]"></div>
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_80%_20%,#06b6d4_0%,transparent_65%)]"></div>
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_60%_80%,#1d4ed8_0%,transparent_70%)]"></div>
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_40%_60%,#2563eb_0%,transparent_55%)]"></div>
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_90%_70%,#0ea5e9_0%,transparent_60%)]"></div>
      </div>

      {/* Animated Energy Grid */}
      <div className="absolute inset-0 opacity-25">
        <div className="absolute inset-0 bg-[linear-gradient(to_right,#3b82f6_1px,transparent_1px),linear-gradient(to_bottom,#3b82f6_1px,transparent_1px)] bg-[size:60px_60px] animate-pulse"></div>
        <div className="absolute inset-0 bg-[linear-gradient(45deg,#06b6d4_1px,transparent_1px),linear-gradient(-45deg,#06b6d4_1px,transparent_1px)] bg-[size:80px_80px] animate-pulse opacity-60" style={{ animationDelay: '1s' }}></div>
      </div>

      {/* Flowing Light Streams */}
      <div className="absolute inset-0 opacity-30">
        <div className="absolute top-0 left-1/4 w-1 h-full bg-gradient-to-b from-transparent via-blue-400 to-transparent animate-pulse"></div>
        <div className="absolute top-0 right-1/3 w-1 h-full bg-gradient-to-b from-transparent via-cyan-400 to-transparent animate-pulse" style={{ animationDelay: '2s' }}></div>
        <div className="absolute left-0 top-1/3 w-full h-1 bg-gradient-to-r from-transparent via-blue-300 to-transparent animate-pulse" style={{ animationDelay: '1.5s' }}></div>
      </div>

      {/* Floating Particles */}
      <div className="absolute inset-0 pointer-events-none">
        {Array.from({ length: 8 }).map((_, i) => (
          <div
            key={i}
            className={`absolute w-2 h-2 bg-primary/30 rounded-full animate-float`}
            style={{
              left: `${10 + (i * 12)}%`,
              top: `${20 + (i * 8)}%`,
              animationDelay: `${i * 0.5}s`,
              animationDuration: `${3 + (i * 0.2)}s`
            }}
          />
        ))}
      </div>

      <div className="container mx-auto px-6 py-20 text-center relative z-10">
        <div className="max-w-5xl mx-auto">
          {/* Glass Card Container */}
          <div className="backdrop-blur-sm bg-card/10 border border-border/20 rounded-3xl p-8 md:p-12 shadow-2xl animate-fade-in">
            {/* Profile Image with Enhanced Effects */}
            <div className="mb-10 relative">
              <div className="relative inline-block">
                <div className="absolute inset-0 bg-accent-gradient rounded-full blur-xl opacity-30 animate-pulse"></div>
                <img
                  src={profileImage}
                  alt="Hussein Osman"
                  className="relative w-36 h-36 md:w-44 md:h-44 rounded-full border-4 border-primary glow-effect object-cover shadow-2xl transition-transform duration-300 hover:scale-110"
                />
                <div className="absolute -bottom-2 -right-2 w-8 h-8 bg-accent rounded-full border-4 border-background flex items-center justify-center">
                  <div className="w-3 h-3 bg-green-400 rounded-full animate-pulse"></div>
                </div>
              </div>
            </div>

            {/* Enhanced Headlines */}
            <div className="space-y-6 mb-10">
              <h1 className="text-5xl md:text-7xl font-bold leading-tight">
                <span className="block text-foreground mb-2">Hi, I'm</span>
                <span className="bg-accent-gradient bg-clip-text text-transparent animate-pulse">
                  Hussein Osman
                </span>
              </h1>
              
              <div className="relative">
                <h2 className="text-2xl md:text-4xl text-primary mb-2 font-semibold">
                  Full Stack Developer
                </h2>
                <div className="mx-auto w-24 h-1 bg-accent-gradient rounded-full"></div>
              </div>
            </div>

            {/* Enhanced Bio with Typing Effect */}
            <div className="mb-12">
              <p className="text-lg md:text-xl text-muted-foreground max-w-4xl mx-auto leading-relaxed">
                Passionate software engineering graduate from{' '}
                <span className="text-primary font-semibold">Moringa School</span>, specializing in building 
                real-world web and mobile solutions with modern technologies. Driven by curiosity and 
                a desire to create{' '}
                <span className="text-accent font-semibold">impactful solutions</span>{' '}
                that improve lives.
              </p>
            </div>

            {/* Enhanced CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-6 justify-center items-center mb-8">
              <Button
                onClick={() => scrollToSection('portfolio')}
                size="lg"
                className="group relative bg-accent-gradient text-accent-foreground hover:glow-effect px-10 py-4 text-lg font-semibold rounded-full transition-all duration-300 hover:scale-105 shadow-lg hover:shadow-2xl"
              >
                <span className="relative z-10">View My Work</span>
                <div className="absolute inset-0 bg-white/20 rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
              </Button>
              <Button
                onClick={() => scrollToSection('contact')}
                variant="outline"
                size="lg"
                className="group border-2 border-primary text-primary hover:bg-primary hover:text-primary-foreground px-10 py-4 text-lg rounded-full transition-all duration-300 hover:scale-105 shadow-lg backdrop-blur-sm bg-background/10"
              >
                Get in Touch
              </Button>
            </div>

            {/* Skills Preview */}
            <div className="flex flex-wrap justify-center gap-3 opacity-70">
              {['React', 'TypeScript', 'Node.js', 'Python', 'MongoDB'].map((skill) => (
                <span
                  key={skill}
                  className="px-4 py-2 bg-muted/20 border border-border/30 rounded-full text-sm font-medium backdrop-blur-sm hover:bg-muted/30 transition-colors duration-300"
                >
                  {skill}
                </span>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Enhanced Floating Elements */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        <div className="absolute top-20 left-10 animate-float opacity-20">
          <div className="w-10 h-10 bg-accent-gradient rounded-2xl rotate-12 shadow-lg"></div>
        </div>
        <div className="absolute top-40 right-20 animate-float opacity-30" style={{ animationDelay: '1s' }}>
          <div className="w-8 h-8 bg-primary rounded-full shadow-lg"></div>
        </div>
        <div className="absolute bottom-40 left-20 animate-float opacity-25" style={{ animationDelay: '2s' }}>
          <div className="w-12 h-12 bg-accent/50 rounded-lg transform rotate-45 shadow-lg"></div>
        </div>
        <div className="absolute top-1/2 right-10 animate-float opacity-20" style={{ animationDelay: '1.5s' }}>
          <div className="w-6 h-6 bg-primary/60 rounded-full shadow-lg"></div>
        </div>
        <div className="absolute bottom-20 right-1/4 animate-float opacity-30" style={{ animationDelay: '0.5s' }}>
          <div className="w-8 h-8 bg-accent-gradient rounded-lg shadow-lg"></div>
        </div>
      </div>
    </section>
  );
};

export default Hero;