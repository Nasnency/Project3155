INSERT into `users` (`username`, `password_hash`, `email`)
VALUES ('aturing', 'b93727798b520dc10d145b53909c061f082ff14cd5f8cb4ab24c3b71bfa57d7e12e1296029be74c06a0d91ba32756f9fc978047fbe7232be67f94dfc1de9ced9', 'alan@enigma.com');

INSERT into `users` (`username`, `password_hash`, `email`)
VALUES ('dritchie', '67aff785bd17ac24448d491926ff7aadd8fa75e51a2f7a9bfc31889bad0adcd2989061a27ccd9eff9e5e31f2bc14b5c193727e116dc8dc48259acb3919171cd4', 'dennis@unix.com');

INSERT into `users` (`username`, `password_hash`, `email`)
VALUES ('llamport', '9171d14954eeda4e70777c23d98e349818125cdaeb884ff97ebf8cc0a9c7778f54ce394256588148132a03ebea891e44077c659e6c0132fa87a8cf77e436ae11', 'leslie@paxos.com');

INSERT into `users` (`username`, `password_hash`, `email`)
VALUES ('bliskov', '1e4b9ae956cad1385cfa6fffd8323dd16c3fe18c54e6447e49bddef2138d042e84e1505a541c6ef19a5026e684b2559efd366145870a0a8d4d4173c0877f6cd2', 'barbara@thor.com');

INSERT into `comic` (`page_name`, `image_url`)
VALUES ('Page1', 'static/images/p1.jpg');

INSERT into `comic` (`page_name`, `image_url`)
VALUES ('Page2', 'static/images/p2.jpg');

INSERT into `comic` (`page_name`, `image_url`)
VALUES ('Page3', 'static/images/p3.jpg');

INSERT into `comic` (`page_name`, `image_url`)
VALUES ('Page4', 'static/images/p4.jpg');

INSERT into `comic` (`page_name`, `image_url`)
VALUES ('Page5', 'static/images/p5.jpg');

INSERT into `comic` (`page_name`, `image_url`)
VALUES ('Page6', 'static/images/p6.jpg');

INSERT into `comment` (`username`, `content`, `comic_page`)
VALUES ('aturing', 'Banging.', `Page1`);