import { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Label } from "@/components/ui/label";
import { useToast } from "@/hooks/use-toast";

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const { toast } = useToast();

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);

    try {
      const response = await fetch('https://formspree.io/f/mldlraeg', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        toast({
          title: "Message Sent!",
          description: "Thank you for your message. I'll get back to you soon!",
        });
        setFormData({ name: '', email: '', message: '' });
      } else {
        toast({
          title: "Error",
          description: "Failed to send message. Please try again.",
          variant: "destructive",
        });
      }
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to send message. Please try again.",
        variant: "destructive",
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  const contactInfo = [
    {
      icon: '📧',
      label: 'Email',
      value: 'huseinkey46@gmail.com',
      href: 'mailto:huseinkey46@gmail.com'
    },
    {
      icon: '📱',
      label: 'WhatsApp',
      value: '0711380969',
      href: 'https://wa.me/254711380969'
    },
    {
      icon: '💻',
      label: 'GitHub',
      value: 'hussein-ft',
      href: 'https://github.com/hussein-ft'
    },
    {
      icon: '📷',
      label: 'Instagram',
      value: 'Huسein ___o5man',
      href: 'https://instagram.com/hussein___o5man'
    }
  ];

  return (
    <section id="contact" className="py-20 bg-background">
      <div className="container mx-auto px-6">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-12">
            Get In <span className="bg-accent-gradient bg-clip-text text-transparent">Touch</span>
          </h2>

          <div className="grid md:grid-cols-2 gap-12">
            {/* Contact Form */}
            <Card className="bg-card-gradient border-border">
              <CardHeader>
                <CardTitle className="text-2xl font-bold text-primary">
                  Send me a message
                </CardTitle>
                <p className="text-muted-foreground">
                  I'd love to hear from you! Whether you have a project in mind, 
                  want to collaborate, or just want to say hello.
                </p>
              </CardHeader>
              <CardContent>
                <form onSubmit={handleSubmit} className="space-y-6">
                  <div className="space-y-2">
                    <Label htmlFor="name" className="text-foreground">Name</Label>
                    <Input
                      id="name"
                      name="name"
                      type="text"
                      placeholder="Your full name"
                      value={formData.name}
                      onChange={handleInputChange}
                      required
                      className="bg-input border-border focus:border-primary"
                    />
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="email" className="text-foreground">Email</Label>
                    <Input
                      id="email"
                      name="email"
                      type="email"
                      placeholder="your.email@example.com"
                      value={formData.email}
                      onChange={handleInputChange}
                      required
                      className="bg-input border-border focus:border-primary"
                    />
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="message" className="text-foreground">Message</Label>
                    <Textarea
                      id="message"
                      name="message"
                      placeholder="Tell me about your project or just say hello..."
                      value={formData.message}
                      onChange={handleInputChange}
                      required
                      rows={5}
                      className="bg-input border-border focus:border-primary resize-none"
                    />
                  </div>

                  <Button
                    type="submit"
                    disabled={isSubmitting}
                    className="w-full bg-accent-gradient text-accent-foreground hover:glow-effect py-6 text-lg font-semibold"
                  >
                    {isSubmitting ? (
                      <span className="flex items-center justify-center">
                        <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-current mr-2"></div>
                        Sending...
                      </span>
                    ) : (
                      'Send Message'
                    )}
                  </Button>
                </form>
              </CardContent>
            </Card>

            {/* Contact Information */}
            <div className="space-y-8">
              <Card className="bg-card-gradient border-border">
                <CardHeader>
                  <CardTitle className="text-2xl font-bold text-primary">
                    Let's connect
                  </CardTitle>
                  <p className="text-muted-foreground">
                    Ready to work together? I'm always open to discussing new opportunities, 
                    creative projects, or potential collaborations.
                  </p>
                </CardHeader>
              </Card>

              {/* Contact Details */}
              <div className="space-y-4">
                {contactInfo.map((info, index) => (
                  <Card key={index} className="bg-card border-border hover:glow-effect smooth-transition">
                    <CardContent className="p-6">
                      <a
                        href={info.href}
                        target={info.href.startsWith('http') ? '_blank' : undefined}
                        rel={info.href.startsWith('http') ? 'noopener noreferrer' : undefined}
                        className="flex items-center space-x-4 hover:text-primary smooth-transition"
                      >
                        <div className="text-2xl">{info.icon}</div>
                        <div>
                          <div className="font-semibold text-foreground">{info.label}</div>
                          <div className="text-muted-foreground">{info.value}</div>
                        </div>
                      </a>
                    </CardContent>
                  </Card>
                ))}
              </div>

              {/* Call to Action */}
              <Card className="bg-accent-gradient border-none">
                <CardContent className="p-8 text-center">
                  <h3 className="text-xl font-bold text-accent-foreground mb-3">
                    Ready to start a project?
                  </h3>
                  <p className="text-accent-foreground/80 mb-4">
                    Let's build something amazing together!
                  </p>
                  <Button
                    asChild
                    variant="secondary"
                    className="bg-background text-foreground hover:bg-background/90"
                  >
                    <a href="mailto:huseinkey46@gmail.com">
                      Start Conversation
                    </a>
                  </Button>
                </CardContent>
              </Card>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Contact;