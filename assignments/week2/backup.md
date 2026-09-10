# Assignment W2.3: Backup My Computer

## a. Why is backing up important?

Backing up my computer is important because I store academic work, programming projects, research files, documents, and personal files that would be difficult or sometimes impossible to recreate if they were lost. A computer can experience hardware failure, file corruption, malware, accidental deletion, or other unexpected problems at any time. Without a backup, losing my computer could also mean losing many hours of work on assignments and projects. A reliable backup gives me another copy of important files so that I can restore them when something goes wrong. It also allows me to recover previous versions of files if I accidentally modify or delete something important. For this reason, I consider regular backups an essential part of protecting both my academic and personal data.

## b. Real-world consequences applying to me

Three consequences that could affect me if I did not have a backup are:

1. **Loss of my academic work:** I could lose assignments, class notes, reports, presentations, or other university files and have to recreate them.
2. **Loss or corruption of programming and research projects (specially my Lab projects are the most important):** Source code, datasets, experiment results, and project configurations could become corrupted or disappear after a disk failure or accidental deletion.
3. **Loss of personal files and time:** Important documents, photographs, and other personal files could be permanently lost, and professional data recovery could be expensive and may not successfully recover everything.

## c. Which backup plan will I use?

I will use a **cloud backup with Microsoft OneDrive**, since I use a Windows computer. I would first sign in to OneDrive using my Microsoft account. Then I would open OneDrive settings and enable backup for important folders such as Documents, Desktop, and Pictures. I would also place important school and project files inside folders synchronized with OneDrive. After setting it up, I would verify that the synchronization is working and periodically check that my important files can be accessed from OneDrive. For programming projects, I would additionally continue using GitHub for version control, but I would not treat GitHub as a replacement for a complete computer backup.

## d. My plan to establish a backup schedule

I will check my backups **every Sunday at 7:00 PM**. My important Documents, Desktop files, university assignments, research documents, and personal files will be synchronized with OneDrive throughout the week. During my Sunday check, I will make sure that OneDrive has completed synchronization and that there are no errors. I will also verify that my current programming projects have their recent changes committed and pushed to their appropriate Git repositories. Once a month, I will check a few backed-up files to make sure that they can actually be opened and restored successfully.

## e. Real-world consequences applying to others

A well-known example, also learned from one of my classes, of the importance of a reliable backup strategy occurred at **GitLab.com in 2017**. During troubleshooting of database replication problems, an engineer accidentally deleted data from GitLab's primary production database. GitLab had several backup and replication mechanisms, but multiple recovery methods were either not configured correctly, were failing, or had not been regularly tested. As a result, GitLab had to restore an approximately six-hour-old database copy and permanently lost several hours of database activity, including information related to projects, comments, user accounts, issues, and snippets. GitLab later estimated that the incident affected roughly 5,000 projects, 5,000 comments, and 700 new user accounts. The incident could have been reduced or avoided by having verified and regularly tested backups, redundant recovery methods, monitoring that immediately reported backup failures, and documented disaster-recovery procedures.
