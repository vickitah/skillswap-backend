import { Card, CardContent } from "@/components/ui/card";

const Skills = () => {
  const frontendSkills = [
    { name: 'HTML', level: 95, color: 'bg-orange-500' },
    { name: 'CSS', level: 90, color: 'bg-blue-500' },
    { name: 'JavaScript', level: 90, color: 'bg-yellow-500' },
    { name: 'React', level: 85, color: 'bg-cyan-500' },
    { name: 'Tailwind CSS', level: 88, color: 'bg-teal-500' }
  ];

  const backendSkills = [
    { name: 'Python', level: 88, color: 'bg-green-500' },
    { name: 'Django', level: 85, color: 'bg-green-600' },
    { name: 'Flask', level: 80, color: 'bg-red-500' },
    { name: 'RESTful APIs', level: 82, color: 'bg-purple-500' }
  ];

  const toolsSkills = [
    { name: 'Git', level: 90, color: 'bg-orange-600' },
    { name: 'GitHub', level: 88, color: 'bg-gray-700' },
    { name: 'VS Code', level: 92, color: 'bg-blue-600' }
  ];

  const databaseSkills = [
    { name: 'SQL', level: 85, color: 'bg-blue-700' },
    { name: 'MongoDB', level: 78, color: 'bg-green-700' }
  ];

  const SkillBar = ({ skill }: { skill: any }) => (
    <div className="space-y-2">
      <div className="flex justify-between items-center">
        <span className="font-medium text-foreground">{skill.name}</span>
        <span className="text-sm text-muted-foreground">{skill.level}%</span>
      </div>
      <div className="w-full bg-muted rounded-full h-2">
        <div
          className={`h-2 rounded-full ${skill.color} transition-all duration-1000 ease-out`}
          style={{ width: `${skill.level}%` }}
        ></div>
      </div>
    </div>
  );

  return (
    <section id="skills" className="py-20 bg-background">
      <div className="container mx-auto px-6">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-12">
            My <span className="bg-accent-gradient bg-clip-text text-transparent">Skills</span>
          </h2>

          <div className="grid md:grid-cols-2 lg:grid-cols-2 gap-8">
            {/* Frontend Skills */}
            <Card className="bg-card-gradient border-border hover:glow-effect smooth-transition">
              <CardContent className="p-8">
                <h3 className="text-2xl font-bold mb-6 text-primary flex items-center">
                  <span className="mr-3">🎨</span>
                  Frontend Development
                </h3>
                <div className="space-y-6">
                  {frontendSkills.map((skill, index) => (
                    <SkillBar key={index} skill={skill} />
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Backend Skills */}
            <Card className="bg-card-gradient border-border hover:glow-effect smooth-transition">
              <CardContent className="p-8">
                <h3 className="text-2xl font-bold mb-6 text-primary flex items-center">
                  <span className="mr-3">⚙️</span>
                  Backend Development
                </h3>
                <div className="space-y-6">
                  {backendSkills.map((skill, index) => (
                    <SkillBar key={index} skill={skill} />
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Tools & DevOps */}
            <Card className="bg-card-gradient border-border hover:glow-effect smooth-transition">
              <CardContent className="p-8">
                <h3 className="text-2xl font-bold mb-6 text-primary flex items-center">
                  <span className="mr-3">🛠️</span>
                  Tools & DevOps
                </h3>
                <div className="space-y-6">
                  {toolsSkills.map((skill, index) => (
                    <SkillBar key={index} skill={skill} />
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Database */}
            <Card className="bg-card-gradient border-border hover:glow-effect smooth-transition">
              <CardContent className="p-8">
                <h3 className="text-2xl font-bold mb-6 text-primary flex items-center">
                  <span className="mr-3">🗄️</span>
                  Database
                </h3>
                <div className="space-y-6">
                  {databaseSkills.map((skill, index) => (
                    <SkillBar key={index} skill={skill} />
                  ))}
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Tech Stack Icons */}
          <div className="mt-16">
            <h3 className="text-xl font-semibold text-center mb-8 text-muted-foreground">
              Technologies I Work With
            </h3>
            <div className="flex flex-wrap justify-center gap-8">
              {[...frontendSkills, ...backendSkills, ...toolsSkills, ...databaseSkills].map((skill, index) => (
                <div
                  key={index}
                  className="tech-icon p-4 bg-card rounded-lg border border-border text-center min-w-[100px]"
                >
                  <div className="text-2xl mb-2">
                    {skill.name === 'HTML' && '🌐'}
                    {skill.name === 'CSS' && '🎨'}
                    {skill.name === 'JavaScript' && '⚡'}
                    {skill.name === 'React' && '⚛️'}
                    {skill.name === 'Tailwind CSS' && '💨'}
                    {skill.name === 'Python' && '🐍'}
                    {skill.name === 'Django' && '🎸'}
                    {skill.name === 'Flask' && '🌶️'}
                    {skill.name === 'RESTful APIs' && '🔗'}
                    {skill.name === 'Git' && '🔀'}
                    {skill.name === 'GitHub' && '🐙'}
                    {skill.name === 'VS Code' && '💻'}
                    {skill.name === 'SQL' && '🗄️'}
                    {skill.name === 'MongoDB' && '🍃'}
                  </div>
                  <span className="text-sm font-medium">{skill.name}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Skills;