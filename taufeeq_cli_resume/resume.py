from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.progress import Progress, BarColumn, TextColumn
from rich.text import Text
from time import sleep

def display_resume():
    # Initialize the console for rendering rich text
    console = Console()

    # Display a loading progress bar
    with Progress(
        TextColumn("[bold cyan]{task.description}[/bold cyan]"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("Loading Taufeeq's Resume...", total=100)
        for _ in range(100):
            sleep(0.02)
            progress.update(task, advance=1)

    resume_content = """
    Hey! I’m Taufeeq Riyaz. I’m obsessed with technology, building communities, and creating meaningful connections. 
    Every challenge I take on is an opportunity to grow, learn, and empower others.

    [bold magenta]Achivements[/bold magenta]
    - Earning a spot on [green]20Under20 by Infosys Springboard[/green] for my entrepreneurship journey.
    - Founding [bold]DevSphere[/bold], a Web3 & Open Source club with RV University.
    - Leading [bold]Tenacity HQ[/bold], a platform that has supported over 150 events. 
    - Mentored 800+ students and collaborated with global companies for impactful workshops. 

    [bold magenta]Top Skills[/bold magenta]
    Marketing | Community Outreach | Python | Open Source | JavaScript | Web3 

    [bold blue]My Journey So Far[/bold blue]

    [bold green]Tenacity HQ | Founder ([bold red]2022-Present[/bold red], [bold cyan]Bangalore[/bold cyan])[/bold green]
    - Built a community of 6,000+ students and professionals, organizing 50+ meetups, hackathons, and workshops. 
    - Engaged 150,000+ participants across colleges and universities.
    - Increased brand visibility by 30% through strategic partnerships with industry leaders.

    [bold green]DevSphere | Founder and President ([bold red]2024-Present[/bold red], [bold cyan]Bangalore[/bold cyan])[/bold green]
    - Founded the first open-source and blockchain club at RV University, securing 200+ registrations on launch day. 
    - Organized 10+ workshops, impacting 1,000+ students and fostering a community around Web3 and open-source tech.

    [bold green]Rabble Labs | Community and Growth Intern ([bold red]2024[/bold red], [bold cyan]Bangalore[/bold cyan])[/bold green]
    - Increased engagement by 20% and improved content quality within the creator community. 
    - Streamlined operations, reducing inefficiencies by 15% and boosting overall engagement.

    [bold green]Spenny (Acquired By CRED) | Chief Experiment Officer ([bold red]2021-2023[/bold red], [bold cyan]Remote[/bold cyan])[/bold green]
    - Collaborated on customer acquisition strategies and enhanced Spenny’s brand presence online.

    [bold green]RV University | Peer Mentor and Teaching Assistant ([bold red]2022-2023[/bold red], [bold cyan]Bangalore[/bold cyan])[/bold green]
    - Mentored 800+ students, including seniors, guiding both academic and career growth. 
    - Organized 30+ workshops in collaboration with 50+ companies, delivering 150+ teaching hours.

    [bold magenta]Education[/bold magenta]
    - RV University (B. Tech. honours in Computer Science With Minors in Fintech, 2023-2027)
    - Y Combinator Startup School (2022) 
    - Alchemy University: Blockchain & Web3 (2023)
    
    [bold cyan]Awards[/bold cyan]
    - [bold]Mission To Mars Student Challenge:[/bold] Worked alongside NASA scientists, engineers, and education staff to contribute code to the Perseverance Rover open-source repository.
    - [bold]BESCOM TIMES POWER WALK NIE Power Project Competition:[/bold] Built a project selected from 120 schools, winning the first runner-up award and titled Bengaluru’s most powerful student. Featured in Times of India, Deccan Herald, and other major newspapers.
    - [bold]National Science Olympiad Gold Medal (2012)[/bold] 
    - [bold]International Math Olympiad Gold Medals (2015, 2016)[/bold] 
    - [bold]National Science Olympiad Silver Medals (2013, 2016)[/bold] 
    - [bold]International Math Olympiad Silver Medals (2013, 2014)[/bold]

    [bold cyan]Let’s Connect![/bold cyan]
    Email: [green]contact.taufeeq@gmail.com[/green]
    LinkedIn: [blue]https://linkedin.com/in/taufeeq[/blue]
    GitHub: [cyan]https://github.com/0xtaufeeq[/cyan]
    """

    # Function to animate sections of the resume with improved UI
    def animate_section(content, title):
        # Create a panel for the section and display it with a live refresh
        panel = Panel(content, title=Text(title, style="bold yellow"), border_style="bright_black", padding=(1, 2), expand=False)
        with Live(console=console, refresh_per_second=4):
            console.print(panel)
            sleep(3)  # Hold the section display for a bit longer

    # Define sections and titles for the resume
    resume_sections = [
        ("[bold cyan]Taufeeq Riyaz[/bold cyan]\n[yellow]Entrepreneur | Community Builder | Developer | Designer[/yellow]", "About Me"),
        ("Hey there! I’m Taufeeq, a passionate techie and community-driven leader obsessed with bridging the gap between technology and human connections. I believe in the power of community, collaboration, and creating impactful experiences. I’m always eager to learn, iterate, and push boundaries.\n\nOver the past few years, I've built vibrant communities like Tenacity HQ and DevSphere, impacting thousands of students and professionals. From organizing hackathons and workshops to connecting with industry leaders, I’m committed to empowering the next generation of builders and creators.", "Summary"),
        (resume_content.split("[bold magenta]Achivements[/bold magenta]")[1].split("[bold magenta]Top Skills[/bold magenta]")[0], "Achivement Highlights"),
        (resume_content.split("[bold magenta]Top Skills[/bold magenta]")[1].split("[bold blue]My Journey So Far[/bold blue]")[0], "Top Skills"),
        (resume_content.split("[bold blue]My Journey So Far[/bold blue]")[1].split("[bold magenta]Education[/bold magenta]")[0], "My Story in Roles"),
        (resume_content.split("[bold magenta]Education[/bold magenta]")[1].split("[bold cyan]Awards[/bold cyan]")[0], "Education"),
        (resume_content.split("[bold cyan]Awards[/bold cyan]")[1].split("[bold cyan]Let’s Connect![/bold cyan]")[0], "Awards"),
        (resume_content.split("[bold cyan]Let’s Connect![/bold cyan]")[1], "Let’s Connect!"),
    ]

    # Display each section using the animate_section function
    for content, title in resume_sections:
        animate_section(content, title)

if __name__ == "__main__":
    display_resume()
