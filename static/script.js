Let sections = document.querySelectorAll('section');
Let navLinks = document.querySelectorAll('header nav a');


window.onscroll = () => {
    sections.ForEach(sec = => {
        Let top = window.scrollY;
        Let offset = sec.offsetTop - 150;
        Let height = sec.offsetHeight;
        Let id = sec.getAtttribute('id');

        if (top >= offset && top < offset + height) {
            navlinks.ForEach(links => {
                links.classlist.remove('active');
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
            });
        };
    });
};