# Contributors

# There are N
# contributors. Each contributor has a name and one or more skills at a specific level (0,1,2,...)

# . Not possessing a skill is equivalent to possessing a skill at level 0.

# For example, three contributors could have the following skills:

#     Anna: Python level 3
#     Bob: C++ level 3
#     Maria: HTML level 4, CSS level 6

class Contributors:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def __str__(self):
        return self.name + ": " + self.skills

    def __repr__(self):
        return self.name + ": " + self.skills

    def __eq__(self, other):
        return self.name == other.name and self.skills == other.skills

    def __hash__(self):
        return hash(self.name)
# Projects

# There are M

# projects. Each project is described by:

#     its name
#     the duration of the project in days (how long it takes to complete a project once it is started)
#     the score awarded for completing the project
#     the “best before” time in days – if the project last day of work is strictly before the indicated day, it earns the full score. If it’s late (that is, the project is still worked on during or after its "best before day"), it gets one point less for each day it is late, but no less than zero points. See also the example in the "Assignments" section below.
#     a list of roles for contributors working on the project

# Each project has one or more roles that need to be filled by contributors. Each role requires one skill at a specific level, and can be filled by a single contributor. Each contributor can fill at most one role on a single project.

# For example, a project called "WebServer" could have the following roles:

#     Role 0 requiring Python level 3
#     Role 1 requiring HTML level 1
#     Role 2 requiring CSS level 5

class Project:
    def __init__(self, name, duration, score, best_before, roles):
        self.name = name
        self.duration = duration
        self.score = score
        self.best_before = best_before
        self.roles = roles

    def __str__(self):
        return self.name + ": " + self.duration + " " + self.score + " " + self.best_before + " " + self.roles

    def __repr__(self):
        return self.name + ": " + self.duration + " " + self.score + " " + self.best_before + " " + self.roles

    def __eq__(self, other):
        return self.name == other.name and self.duration == other.duration and self.score == other.score and self.best_before == other.best_before and self.roles == other.roles

    def __hash__(self):
        return hash(self.name)
# Filling roles and mentorship

# A contributor can be assigned to a project for a specific role (at most one role in a single project), if they either:

#     have the skill at the required level or higher; or
#     have the skill at exactly one level below the required level, only if another contributor on the same project (assigned to another role), has this skill at the required level or higher. In this case, the contributor will be mentored by their colleague :)

# One contributor can mentor multiple people at once, including for the same skill. A contributor can mentor and be mentored by other contributors at the same time.

# Not possessing a skill is equivalent to possessing a skill at level 0. So a contributor can work on a project and be assigned to a role with requirement C++ level 1 if they don’t know any C++, provided that somebody else on the team knows C++ at level 1 or higher.

# For example:

# For the project WebServer above we could make the following assignments:

# Role 0 (requires Python level 3) is assigned to Anna (Python level 3).

#     ☑️ Anna has the same level in Python as required.

# Role 1 (requires HTML level 1) is assigned to Bob (C++ level 3).

#     ⚠ Bob has level 0 in HTML. Since his level is only one below required, he can be assigned, but must be mentored by another contributor who knows HTML at level 1 or above.

# Role 2 (requires CSS level 5) is assigned to Maria (HTML level 4, CSS level 6)

#     ☑️ Maria has a higher level than the one required for CSS.
#     ☑️ Maria can mentor Bob on HTML since she has HTML level 4.
def mentor_mentor(contributors, project, role):
    for contributor in contributors:
        if contributor.skills == role.skill:
            return True
        elif contributor.skills < role.skill:
            for other_contributor in contributors:
                if other_contributor.skills == role.skill:
                    return True
    return False
# Assignments

# Each contributor can start working on day 0 and can be working on at most one project at the same time. Once the work on a project starts, its contributors will be working on it the number of days equal to its duration and then become available to work on other projects.

# For example, if the project WebServer has duration of 7 days and starts on day 0, the contributors assigned to it will be working on it during: day 0, day 1, day 2, day 3, day 4, day 5 and day 6. On day 7 the project is already completed. Contributors assigned to it can work on another project on day 7.
def assign_contributors(contributors, projects):
    for project in projects:
        for role in project.roles:
            for contributor in contributors:
                if contributor.skills == role.skill:
                    return True
                elif contributor.skills < role.skill:
                    for other_contributor in contributors:
                        if other_contributor.skills == role.skill:
                            return True
    return False
# Learning

# Completing a project is a learning opportunity, especially for the contributors working on the edge of their existing abilities! When each project is completed:

#     contributors working in roles where the required skill level was equal or higher than their current level improve their skill level by one level
#     other contributors keep their skill level

# Note that mentoring someone doesn’t increase the level of the skill for the mentor.

# For example:

# In the assignments above:

#     Anna improves Python skill to level 4;
#     Bob improves HTML skill to level 1;
#     Maria improves neither the CSS skill (because Maria’s CSS is already at a level higher than required) nor the HTML skill (because her role required CSS, not HTML).
def learn(contributors, projects):
    for project in projects:
        for contributor in contributors:
            for role in project.roles:
                if contributor.skills == role.skill:
                    if contributor.skills < role.skill:
                        contributor.skills += 1
                    else:
                        continue
                elif contributor.skills < role.skill:
                    for other_contributor in contributors:
                        if other_contributor.skills == role.skill:
                            other_contributor.skills += 1
                            break
                        else:
                            continue
                else:
                    continue
    return contributors
# The main function
def main():
    # read input
    with open("src/lib/hashc/input_data/a_an_example.in.txt", 'r') as f:
        lines = f.readline().rstrip('\n').split(' ')
        #readlines()
        # number of projects
        M = int(lines[1])
        # number of contributors
        N = int(lines[0])
           
        # number of skills
        #S = int(lines[2])
        # contributors
        contributors = []
        for i in range(N):
            contributor_line = f.readline().rstrip('\n').split(' ')
            #self, name, skills
            name = contributor_line[0]
            skills = int(contributor_line[1])
            contributors.append(Contributors(name, skills))
        # projects
        projects = []
        for i in range(M):
            #name, duration, score, best_before, roles
            lines = f.readline().split(' ')
            name = lines[0]
            duration = int(lines[1])
            score = int(lines[2]) 
            #IndexError: list index out of range
            best_before = lines[3]
            roles = []
            project = Project(name, duration, score, best_before, roles)
            #skills defaultdict
            skills = []
            for j in range(int(roles)):
                skill = f.readline().split(' ')
                skills[skill[0]] = int(skill[1])
            project.roles = skills
            projects.append(project)
        
        # print(projects)
        # print(contributors)
        # assign contributors
        if assign_contributors(contributors, projects):
            print("YES")
        else:
            print("NO")
        # learn
        learn(contributors, projects)
        # print(contributors)
        # print(projects)
# run program
if __name__ == "__main__":
    main()