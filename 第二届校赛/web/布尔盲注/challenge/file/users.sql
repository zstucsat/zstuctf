SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;
CREATE DATABASE hn13;
CREATE USER 'zstuctf'@'%' IDENTIFIED BY 'HFngixvf52!';
GRANT ALL PRIVILEGES ON hn13.* TO 'zstuctf'@'%';
FLUSH PRIVILEGES;
USE hn13;
-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'admin', 'hint{hn13_l0ve5_5ql1nj3cti0n_F14ghgng1g3g.php}');

SET FOREIGN_KEY_CHECKS = 1;
