# Really Useful Logging and Event Repository (RULER) Project

## What is the RULER project?

I was often coming across issues where I would see logs from different applications and thought there has to be a good way of recording what we should be looking for in a forensic investigation.

For example - what are the quick wins in a remote access application to identify when it was used.
Or what types of useful information can be found for a specific anti-virus application (especially if it encodes the data)

Some of this information is based on my own personal testing, others is compiled documentation found online directly from the vendors or other researchers.

!!! error "Caveat Emptor"
    It should be noted that this information should be used as a guide only. What is and isn't recorded by an application may be similar across products made by an organisation, or may be vastly different between application versions. Should you choose to rely on this information without testing it for yourself you do so at your own risk.

!!! info
    For more riguourous testing and documentation I suggest that you document your findings in a blog, and obtain a degree of verificaiton and validation through the [DFIR Review project](https://dfir.pubpub.org/).

## What is the RULER project not?

Currently I have no plans on documenting 'what you should log', this is more about what is enabled by default.

Some great projects to look at include [What2log](https://what2log.com/) and the [Windows logging cheat sheets](https://www.malwarearchaeology.com/cheat-sheets/)

## Roadmap

- [ ] Include other types of logs such as mail and web server logs for different applications, or different file sharing solutions. Stubs have been made, documentation has not been created.
- [ ] Store the data in a YAML or database format and generate the MK files to allow for ingestion into other tools. This would likely be a fairly large undertaking and without thoroughly testing all versions of all products regularly this may be more effort than it's worth.

## How to contribute

All the source files are on Github. Please make sure to reference where appropirate.
This is still very much a work in progress.

If you have any suggestions or want to contribute, please submit an issue or pull request.
