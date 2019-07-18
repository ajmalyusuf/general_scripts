
--
-- Table structure for table `tasks`
--

DROP TABLE IF EXISTS `tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tasks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `service` varchar(60) DEFAULT NULL,
  `name` varchar(60) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `component` varchar(60) DEFAULT NULL,
  `yaml_name` varchar(128) DEFAULT NULL,
  `ss_bundle` varchar(1024) DEFAULT NULL,
  `recommendation` varchar(32000) DEFAULT NULL,
  `show_results` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_tasks_service` (`service`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES (1,'HDFS','1.1.0 Long GC Pause','Most NN crash is because of garbage collector pause','Namenode','hdfs_runbook_1_1_0.yaml','built-in/example_data/bundle_dir/a-00000000-c-00000000_cokekerbhdp242_0_2017-12-07_04-21-54.tgz','https://docs.google.com/document/d/1FsdibiwLJr1IEshcZCkZaGt6vX3HnGaJdPDUYshPG-Y/edit',1),(2,'HDFS','1.1.1 Group lookup response delay (LDAP)','If the LDAP server is slow to process group lookups, it can hold up NameNode RPC handler threads and affect service','Namenode','hdfs_runbook_1_1_1.yaml','built-in/example_data/bundle_dir/a-00000000-c-00000000_cokekerbhdp242_0_2017-12-07_04-21-54.tgz','https://docs.google.com/document/d/1FsdibiwLJr1IEshcZCkZaGt6vX3HnGaJdPDUYshPG-Y/edit',1),(5,'HDFS','1.1.2 Flush failed for required journals','Namenode has to shut down because it cannot write edits to the minimum of the journal nodes. Root cause lies under the journalnodes','Namenode','hdfs_runbook_1_1_2.yaml','built-in/example_data/bundle_dir/a-00000000-c-00000000_cokekerbhdp242_0_2017-12-07_04-21-54.tgz','https://docs.google.com/document/d/1FsdibiwLJr1IEshcZCkZaGt6vX3HnGaJdPDUYshPG-Y/edit',1),(6,'HDFS','1.1.3 Slow transaction sync to journalnode disks','Another potential problem where namenode will go down is that syncing the transactions to disk is rather slow on the JNs. Namenode has a default write timeout (20 sec)','Namenode','hdfs_runbook_1_1_3.yaml','built-in/example_data/bundle_dir/a-00000000-c-00000000_cokekerbhdp242_0_2017-12-07_04-21-54.tgz','https://docs.google.com/document/d/1FsdibiwLJr1IEshcZCkZaGt6vX3HnGaJdPDUYshPG-Y/edit',1);
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'ajmal@myweb.com','ajmal','ajmal','ajmal','pbkdf2:sha256:50000$l1uRRyhG$589fece9b4bf22106399f531158a393be33fdeb47f7b633673926ca6c72f4712',1),(2,'admin@myweb.com','admin','admin','admin','pbkdf2:sha256:50000$YEhUlpIp$726685aef566bb7f0808e9fb61095e35f0b7ad8cc7f177b91130067bcb673abe',1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

