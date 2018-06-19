# Reading List

<!-- MarkdownTOC autolink="true" autoanchor="true" markdown_preview="github" -->

- [Overview](#overview)
- [Contributing](#contributing)
- [Resources](#resources)
    - [Software Engineering](#software-engineering)
        - [Clean Code by Robert C. Martin](#clean-code-by-robert-c-martin)
        - [Refactoring by Martin Fowler](#refactoring-by-martin-fowler)
    - [Scientific Computing](#scientific-computing)
        - [Good Enough Practices in Scientific Computing, Wilson et al.](#good-enough-practices-in-scientific-computing-wilson-et-al)
            - [Few extra thoughts from Zeb](#few-extra-thoughts-from-zeb)

<!-- /MarkdownTOC -->


<a id="overview"></a>
## Overview

<a id="contributing"></a>
## Contributing

<a id="resources"></a>
## Resources

Issue to make: we could use a common syntax (e.g. yaml or json) for documenting resources and then write a quick conversion script to get them into a common format below (ensures we don't make typos/have inconsistent formatting).

<a id="software-engineering"></a>
### Software Engineering

<a id="clean-code-by-robert-c-martin"></a>
#### Clean Code by Robert C. Martin

- availability
    - [Book Depository](https://www.bookdepository.com/Clean-Code-Robert-C-Martin/9780132350884)
    - [Free pdf, no disclaimer about legality](http://oceanofpdf.com/pdf-epub-clean-code-a-handbook-of-agile-software-craftsmanship-download/)
- recommendation: essential
- price: free?
- length: very long (450 pages, 10 hours +)
- required: all
- ease of use: moderate

<a id="refactoring-by-martin-fowler"></a>
#### Refactoring by Martin Fowler

- availability
    - [Book Depository](https://www.bookdepository.com/Refactoring-Martin-Fowler/9780201485677)
    - [Free pdf, no disclaimer about legality](https://www.csie.ntu.edu.tw/~r95004/Refactoring_improving_the_design_of_existing_code.pdf)
- recommendation: highly
- price: free?
- length: very long (300 pages, 10 hours +)
- required: Ch. 1, 2, 3, 4, 13, 14, 15
- ease of use: moderate

<a id="scientific-computing"></a>
### Scientific Computing

<a id="good-enough-practices-in-scientific-computing-wilson-et-al"></a>
#### Good Enough Practices in Scientific Computing, Wilson et al.

- availability
    - [Free pdf](https://arxiv.org/pdf/1609.00037v2.pdf)
- recommendation: high (although I don't agree with all advice)
- price: free
- length: moderate (20 pages, 20 minutes)
- required: all
- ease of use: all

<a id="few-extra-thoughts-from-zeb"></a>
##### Few extra thoughts from Zeb

If I were using a computer for science, I would rank the most important bits as:

1. tests
    - these are your sanity checks, every scientist is trained to do them, computers should be no different
1. make (or other automatic build software)
    - check that your workflows are reproducible, it will help you (piece of mind if a computer dies) and other researchers
1. continuous integration
    - let someone else do the hardwork of running all the tests for you
1. read 'Good Enough Practices in Scientific Computing' and ask for help from a software engineer
    - they're worth it, even if they're not around that long
1. autodocs/sphinx
    - writing documentation is hard, let it be built for you if you can
    - *note:* I haven't done this yet so it's a distant fifth
