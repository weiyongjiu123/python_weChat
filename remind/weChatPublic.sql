/*
Navicat MySQL Data Transfer

Source Server         : 39.108.130.94_3306
Source Server Version : 50718
Source Host           : 39.108.130.94:3306
Source Database       : weChatPublic

Target Server Type    : MYSQL
Target Server Version : 50718
File Encoding         : 65001

Date: 2017-12-24 12:26:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(12) NOT NULL AUTO_INCREMENT,
  `openId` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `schedule` text CHARACTER SET utf8,
  `subscribe` int(1) DEFAULT NULL COMMENT '用户是否还在继续关注公众号',
  `login` int(1) DEFAULT '0' COMMENT '用户是否登录了',
  `dayRemind` int(1) DEFAULT '1',
  `beforeRemind` int(1) DEFAULT '1',
  `todaySchedule` varchar(500) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
