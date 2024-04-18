# directions (from solicitation)

To facilitate the early recruitment of a conflict-free review panel and ensure
that proposals are submitted to the appropriate category, a Notice of Intent
(NOI) should be submitted by the due date given in Tables 2 and 3 of
ROSES-2024. The NOI is strongly encouraged but not mandatory.

As part of the NOI, the proposer must submit a short description of the
project, the type of award (Foundational or Sustainment), the license for the
project, the list of coinvestigators, and up to five experts qualified to
review their proposal.

NASA does not expect to provide feedback in response to the NOI. In exceptional
cases, feedback may be provided if the type of award or license of the project
is not appropriate.

# Summary directions (per nspires form)

Please read the solicitation carefully. If the solicitation provides
instructions about the content or length of this section, please provide what
the solicitation requests. If no specific guidance is provided, please enter a
brief description of the proposal that provides the information listed below:

- A description of the key, central objectives of the proposal in terms
  understandable to a nonspecialist;
- A concise statement of the methods/techniques proposed to accomplish the
  stated research objectives; and
- A statement of the perceived significance of the proposed work to the
  objectives of the solicitation and to NASA interests and programs in general.

The proposal summary is limited to 4000 characters (including hidden ones when
pasting in from a word processing program). Please avoid special characters or
formatting. If you exceed the limit you will know because you will get a
'Validation Error' message.


# Title

Sustainment of Matplotlib and Cartopy


# Summary (aka a short description of the project)

[at ~3300char]

Matplotlib is a comprehensive library for creating static, animated, and
interactive visualizations in Python.  It is one of the foundational open
source library in the scientific Python ecosystem.  Matplotlib is widely used
across the Astrophysics, Earth Science, Heliophysics, and Planetary Science
divisions of NASA SMD.

Cartopy is a Python package designed to make drawing maps for data analysis and
visualization easy.  Cartopy is built on top of Matplotlib and provides the
projections required for geo-spatial visualizations.  Cartopy is currently used
in the Earth Science division.

We propose three main thrust of work:

 - the ongoing maintenance and incremental development of both libraries,
 - the adoption of new Matplotlib data model into cartopy
 - the targeted support of NASA missions.


The first component of the proposed work is the continued maintenance of both
libraries and their communities.  Maintenance covers a wide range of tasks
including triaging and fixing bugs, reviewing Pull Requests, tagging and
building releases, keeping the continuous integration services running, and
mentoring new contributors.  These tasks are essential for the projects'
health; though each individually is small, they are frequently time critical
and sometimes tedious.  It is unfair and impractical to rely solely on
volunteers to accomplish such tasks.

In addition to on-going and routine maintenance, there are substantial but
incremental enhancements that require long blocks of dedicated effort to
implement.  Without supported developers, such projects can drag out for months
to years or stall altogether.  Examples include fixing long-standing rendering
and performance issues, overhauling build systems to match the changing Python
ecosystem, homogenizing and smoothing the API, and new user-facing
functionality.

Maintenance is not limited to the technical aspects of the project.  Supported
developers improve the management of the project.  We now have the time and
bandwidth to make strategic decisions about the direction of the project to
ensure the long term health and viability of Matplotlib and cartopy.  An
important part of project management is community management: fostering,
diversifying, and growing our communities.  Supported developers are able to
perform outreach: attending conferences, mentoring sprints, or teaching
tutorials.  We must ensure that our community is open and welcoming to everyone
who wants to join, with opportunities to contribute in a spectrum of roles as
their interests and skills develop.

Matplotlib has an ongoing project to modernize how we access and manage
user-supplied data structures (supported by a current grant from NASA
(ROSES-2020)).  We anticipate that this work will be available in the main
library and general use by the end of calendar year 2025.  We propose to
refactor cartopy to use the new Matplotlib implementation.  This will both
improve cartopy and serve as a reference implementation for other
domains-specific libraries on how to fully utilize Matplotlib.

Finally, we will identify, one or more NASA missions to partner with to ensure
that upstream we are fully meeting their needs and that they are using the
tools in an optimal way to address the science needs of their users.

# Type of award

Foundational
