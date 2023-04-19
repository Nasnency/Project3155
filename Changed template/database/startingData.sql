INSERT into `users` (
    `username`
,   `password_salt`
,   `password_hash`
,   `email`
,   `first_name`
,   `last_name`
,   `session_type`)
VALUES (
    'testauthor'
,   '83a4607665b768f6d6646a0e82f7dea7'
,   '13438737c4c08ccaf5fde3be96581581d70ffd403f3458f3445fcd54b330fcb682dec05467589ebb140ba4675051954c2333c00d4410ec733fd3995b395e8811'
,   'author@test.com'
,   'author'
,   'test'
,   1
);

INSERT into `users` (
    `username`
,   `password_salt`
,   `password_hash`
,   `email`
,   `first_name`
,   `last_name`
,   `session_type`)
VALUES (
    'testreader'
,   'd65e09d68dc8a81a850c9e94df8b3cab'
,   '107f0095c60f39c99b1c2d00aafc3785ed01554da645d7c9c60ea32475b0c9f2a4988435952a78e91589efaaf0390486b072c787177b76919d95231a5404660c'
,   'reader@test.com'
,   'reader'
,   'test'
,   0
);


--INSERT into `users` (`username`, `password_hash`, `email`)
--VALUES ('llamport', '9171d14954eeda4e70777c23d98e349818125cdaeb884ff97ebf8cc0a9c7778f54ce394256588148132a03ebea891e44077c659e6c0132fa87a8cf77e436ae11', 'leslie@paxos.com');

--INSERT into `users` (`username`, `password_hash`, `email`)
--VALUES ('bliskov', '1e4b9ae956cad1385cfa6fffd8323dd16c3fe18c54e6447e49bddef2138d042e84e1505a541c6ef19a5026e684b2559efd366145870a0a8d4d4173c0877f6cd2', 'barbara@thor.com');

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

INSERT into `comment` (`username`, `content`, `comic_id`)
VALUES ('testreader', 'Banging.', 'Page1');