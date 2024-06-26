from typing import List

# pylint: disable=too-many-lines
types = [
    "AWS::CDK::Metadata",
    "Module",
    "AWS::CE::AnomalySubscription",
    "AWS::Shield::DRTAccess",
    "AWS::Glue::Partition",
    "AWS::EC2::TransitGatewayRouteTablePropagation",
    "AWS::Shield::ProactiveEngagement",
    "AWS::ApiGateway::BasePathMapping",
    "AWS::GuardDuty::Filter",
    "AWS::ECS::Service",
    "AWS::RAM::ResourceShare",
    "AWS::DMS::ReplicationConfig",
    "AWS::DynamoDB::Table",
    "AWS::AmazonMQ::ConfigurationAssociation",
    "AWS::EC2::SecurityGroupEgress",
    "AWS::Config::OrganizationConfigRule",
    "AWS::Glue::DataQualityRuleset",
    "AWS::Route53Profiles::ProfileAssociation",
    "AWS::Config::ConfigurationRecorder",
    "AWS::CloudFront::ContinuousDeploymentPolicy",
    "AWS::ECR::ReplicationConfiguration",
    "AWS::AppConfig::ExtensionAssociation",
    "AWS::EC2::IPAMPoolCidr",
    "AWS::Redshift::ClusterSubnetGroup",
    "AWS::RDS::DBInstance",
    "AWS::EC2::VPCDHCPOptionsAssociation",
    "AWS::ApiGateway::Model",
    "AWS::EC2::NetworkAcl",
    "AWS::Lambda::EventSourceMapping",
    "AWS::Logs::ResourcePolicy",
    "AWS::DMS::InstanceProfile",
    "AWS::EC2::NetworkAclEntry",
    "AWS::Transfer::Certificate",
    "AWS::ApiGateway::DocumentationPart",
    "AWS::Route53Profiles::Profile",
    "AWS::CloudWatch::CompositeAlarm",
    "AWS::Route53Resolver::FirewallDomainList",
    "AWS::Redshift::EndpointAccess",
    "AWS::AppConfig::Application",
    "AWS::OpsWorks::Stack",
    "AWS::GameLift::Fleet",
    "AWS::DataSync::LocationFSxWindows",
    "AWS::GameLift::Build",
    "AWS::ApiGateway::RequestValidator",
    "AWS::AutoScaling::WarmPool",
    "AWS::ApplicationAutoScaling::ScalableTarget",
    "AWS::Config::StoredQuery",
    "AWS::ACMPCA::Permission",
    "AWS::Transfer::Server",
    "AWS::ApiGateway::DomainName",
    "AWS::ECS::PrimaryTaskSet",
    "AWS::AutoScaling::AutoScalingGroup",
    "AWS::WAFv2::RegexPatternSet",
    "AWS::EKS::FargateProfile",
    "AWS::Route53::DNSSEC",
    "AWS::Redshift::EndpointAuthorization",
    "AWS::EC2::TransitGatewayRouteTable",
    "AWS::ControlTower::EnabledControl",
    "AWS::Route53::RecordSet",
    "AWS::EKS::AccessEntry",
    "AWS::ElastiCache::SecurityGroup",
    "AWS::OpsWorks::Layer",
    "AWS::KinesisFirehose::DeliveryStream",
    "AWS::ImageBuilder::Component",
    "AWS::Glue::Connection",
    "AWS::IAM::Group",
    "AWS::Organizations::ResourcePolicy",
    "AWS::EC2::TransitGatewayMulticastGroupSource",
    "AWS::Transfer::Profile",
    "AWS::GameLift::Alias",
    "AWS::ApiGateway::UsagePlanKey",
    "AWS::CloudFront::RealtimeLogConfig",
    "AWS::LakeFormation::DataCellsFilter",
    "AWS::DataSync::LocationHDFS",
    "AWS::MSK::Cluster",
    "AWS::SecurityHub::DelegatedAdmin",
    "AWS::ControlTower::EnabledBaseline",
    "AWS::EC2::VPCEndpointConnectionNotification",
    "AWS::CodePipeline::Pipeline",
    "AWS::OpsWorks::Instance",
    "AWS::Config::ConfigurationAggregator",
    "AWS::ImageBuilder::ImagePipeline",
    "AWS::ElasticLoadBalancingV2::ListenerCertificate",
    "AWS::Route53Resolver::ResolverRuleAssociation",
    "AWS::FSx::StorageVirtualMachine",
    "AWS::Synthetics::Canary",
    "AWS::SNS::Subscription",
    "AWS::EC2::NatGateway",
    "AWS::Transfer::Workflow",
    "AWS::AppConfig::DeploymentStrategy",
    "AWS::Glue::DevEndpoint",
    "AWS::ElastiCache::UserGroup",
    "AWS::Logs::DeliveryDestination",
    "AWS::ImageBuilder::ImageRecipe",
    "AWS::ApiGateway::RestApi",
    "AWS::OpsWorks::ElasticLoadBalancerAttachment",
    "AWS::S3ObjectLambda::AccessPointPolicy",
    "AWS::ElastiCache::ReplicationGroup",
    "AWS::StepFunctions::StateMachineAlias",
    "AWS::Route53Profiles::ProfileResourceAssociation",
    "AWS::Glue::Job",
    "AWS::Route53::HostedZone",
    "AWS::EKS::PodIdentityAssociation",
    "AWS::ResourceExplorer2::Index",
    "AWS::Glue::Table",
    "AWS::Logs::MetricFilter",
    "AWS::Lambda::Function",
    "AWS::SNS::Topic",
    "AWS::Backup::BackupSelection",
    "AWS::DataSync::LocationFSxLustre",
    "AWS::Logs::DeliverySource",
    "AWS::EC2::VPCGatewayAttachment",
    "AWS::CloudTrail::Trail",
    "AWS::EC2::VPNConnectionRoute",
    "AWS::EC2::InternetGateway",
    "AWS::EC2::GatewayRouteTableAssociation",
    "AWS::WAFv2::IPSet",
    "AWS::SSM::Document",
    "AWS::IAM::Role",
    "AWS::ElastiCache::ServerlessCache",
    "AWS::CloudFront::CloudFrontOriginAccessIdentity",
    "AWS::ApiGateway::ApiKey",
    "AWS::AutoScaling::LaunchConfiguration",
    "AWS::ApiGateway::ClientCertificate",
    "AWS::KinesisAnalyticsV2::Application",
    "AWS::Lambda::Alias",
    "AWS::WAF::IPSet",
    "AWS::EC2::TransitGatewayMulticastDomainAssociation",
    "AWS::WAF::SizeConstraintSet",
    "AWS::EC2::TransitGatewayRouteTableAssociation",
    "AWS::AppConfig::Environment",
    "AWS::ImageBuilder::Image",
    "AWS::ElastiCache::SecurityGroupIngress",
    "AWS::RDS::DBProxyTargetGroup",
    "AWS::CloudWatch::Dashboard",
    "AWS::CloudWatch::Alarm",
    "AWS::GuardDuty::Member",
    "AWS::CloudFormation::CustomResource",
    "AWS::WAFv2::RuleGroup",
    "AWS::ElastiCache::ParameterGroup",
    "AWS::NetworkFirewall::LoggingConfiguration",
    "AWS::Glue::Classifier",
    "AWS::CodeDeploy::DeploymentGroup",
    "AWS::CloudFormation::StackSet",
    "AWS::EC2::Route",
    "AWS::CloudFormation::HookVersion",
    "AWS::RolesAnywhere::Profile",
    "AWS::XRay::ResourcePolicy",
    "AWS::WAFv2::LoggingConfiguration",
    "AWS::DynamoDB::GlobalTable",
    "AWS::Backup::BackupPlan",
    "AWS::ImageBuilder::DistributionConfiguration",
    "AWS::LakeFormation::Permissions",
    "AWS::ResourceExplorer2::View",
    "AWS::Glue::DataCatalogEncryptionSettings",
    "AWS::CloudFront::PublicKey",
    "AWS::IdentityStore::Group",
    "AWS::RAM::Permission",
    "AWS::DataSync::Task",
    "AWS::ECS::TaskDefinition",
    "AWS::Shield::Protection",
    "AWS::IdentityStore::GroupMembership",
    "AWS::EC2::SpotFleet",
    "AWS::IoT::PolicyPrincipalAttachment",
    "AWS::MSK::BatchScramSecret",
    "AWS::S3::Bucket",
    "AWS::GuardDuty::IPSet",
    "AWS::ServiceDiscovery::HttpNamespace",
    "AWS::EMR::SecurityConfiguration",
    "AWS::CloudWatch::InsightRule",
    "AWS::ApiGateway::UsagePlan",
    "AWS::Batch::SchedulingPolicy",
    "AWS::Athena::WorkGroup",
    "AWS::IAM::ServerCertificate",
    "AWS::GlobalAccelerator::CrossAccountAttachment",
    "AWS::Events::EventBus",
    "AWS::SQS::QueueInlinePolicy",
    "AWS::Organizations::Organization",
    "AWS::SSM::MaintenanceWindowTarget",
    "AWS::ApiGateway::Authorizer",
    "AWS::IAM::Policy",
    "AWS::RDS::DBSecurityGroupIngress",
    "AWS::SecurityHub::OrganizationConfiguration",
    "AWS::EC2::TransitGatewayMulticastGroupMember",
    "AWS::EC2::VolumeAttachment",
    "AWS::Glue::SecurityConfiguration",
    "AWS::NetworkFirewall::TLSInspectionConfiguration",
    "AWS::ECS::ClusterCapacityProviderAssociations",
    "AWS::AppConfig::ConfigurationProfile",
    "AWS::Route53Resolver::FirewallRuleGroup",
    "AWS::MSK::Configuration",
    "AWS::EC2::TransitGateway",
    "AWS::EC2::VPCEndpointServicePermissions",
    "AWS::SSM::MaintenanceWindowTask",
    "AWS::EC2::TransitGatewayMulticastDomain",
    "AWS::VerifiedPermissions::PolicyTemplate",
    "AWS::EKS::Cluster",
    "AWS::EFS::FileSystem",
    "AWS::Logs::QueryDefinition",
    "AWS::SecurityHub::ProductSubscription",
    "AWS::IAM::InstanceProfile",
    "AWS::DataSync::LocationNFS",
    "AWS::CertificateManager::Certificate",
    "AWS::SDB::Domain",
    "AWS::EC2::SubnetRouteTableAssociation",
    "AWS::ImageBuilder::ContainerRecipe",
    "AWS::EFS::AccessPoint",
    "AWS::Redshift::ClusterSecurityGroupIngress",
    "AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation",
    "AWS::ElasticLoadBalancingV2::LoadBalancer",
    "AWS::OpenSearchService::Domain",
    "AWS::ServiceDiscovery::Instance",
    "AWS::Elasticsearch::Domain",
    "AWS::EC2::NetworkInterfacePermission",
    "AWS::ServiceDiscovery::PrivateDnsNamespace",
    "AMZN::SDC::Deployment",
    "AWS::SecretsManager::ResourcePolicy",
    "AWS::CloudFormation::HookDefaultVersion",
    "AWS::Config::ConfigRule",
    "AWS::ImageBuilder::Workflow",
    "AWS::ECS::TaskSet",
    "AWS::ACMPCA::CertificateAuthorityActivation",
    "AWS::GuardDuty::ThreatIntelSet",
    "AWS::EC2::VPC",
    "AWS::ARCZonalShift::ZonalAutoshiftConfiguration",
    "AWS::MSK::VpcConnection",
    "AWS::DataSync::LocationAzureBlob",
    "AWS::Logs::LogStream",
    "AWS::Route53::RecordSetGroup",
    "AWS::CloudFormation::PublicTypeVersion",
    "AWS::OpsWorks::App",
    "AWS::Kinesis::Stream",
    "AWS::Batch::JobDefinition",
    "AWS::IAM::SAMLProvider",
    "AWS::CloudFront::KeyGroup",
    "AWS::EC2::NetworkInterfaceAttachment",
    "AWS::EC2::TransitGatewayAttachment",
    "AWS::Glue::CustomEntityType",
    "AWS::CodeDeploy::DeploymentConfig",
    "AWS::StepFunctions::StateMachineVersion",
    "AWS::ServiceCatalogAppRegistry::Application",
    "AWS::Glue::Database",
    "AWS::Backup::BackupVault",
    "AWS::EC2::CustomerGateway",
    "AWS::IAM::GroupPolicy",
    "AWS::WAF::ByteMatchSet",
    "AWS::EC2::Host",
    "AWS::EC2::RouteTable",
    "AWS::RDS::DBProxyEndpoint",
    "AWS::DataSync::LocationSMB",
    "AWS::SecurityHub::Standard",
    "AWS::RolesAnywhere::CRL",
    "AWS::SNS::TopicInlinePolicy",
    "AWS::Redshift::ClusterParameterGroup",
    "AWS::Organizations::Policy",
    "AWS::Glue::Trigger",
    "AWS::GlobalAccelerator::Listener",
    "AWS::VerifiedPermissions::PolicyStore",
    "AWS::EC2::VPCPeeringConnection",
    "AWS::SNS::TopicPolicy",
    "AWS::NetworkFirewall::RuleGroup",
    "AWS::DataSync::LocationFSxOpenZFS",
    "AWS::KMS::Key",
    "AWS::Route53Resolver::ResolverDNSSECConfig",
    "AWS::Route53Resolver::FirewallRuleGroupAssociation",
    "AWS::Route53Resolver::ResolverQueryLoggingConfig",
    "AWS::EC2::SnapshotBlockPublicAccess",
    "AWS::EC2::Subnet",
    "AWS::S3ObjectLambda::AccessPoint",
    "AWS::WAF::Rule",
    "AWS::ElasticBeanstalk::ConfigurationTemplate",
    "AWS::SQS::QueuePolicy",
    "AWS::ApiGateway::Account",
    "AWS::WAFv2::WebACL",
    "AWS::GlobalAccelerator::EndpointGroup",
    "AWS::EC2::SecurityGroup",
    "AWS::EC2::CapacityReservationFleet",
    "AWS::OpsWorks::Volume",
    "AWS::IAM::UserToGroupAddition",
    "AWS::Events::Rule",
    "AWS::CloudFront::KeyValueStore",
    "AWS::GuardDuty::MalwareProtectionPlan",
    "AWS::EC2::VPNGatewayRoutePropagation",
    "AWS::Glue::Crawler",
    "AWS::CloudFront::Function",
    "AWS::ApiGateway::Method",
    "AWS::SSM::PatchBaseline",
    "AWS::ServiceDiscovery::Service",
    "AWS::CloudFront::MonitoringSubscription",
    "AWS::EFS::MountTarget",
    "AWS::EC2::VPNConnection",
    "AWS::WAF::WebACL",
    "AWS::ServiceDiscovery::PublicDnsNamespace",
    "AWS::Shield::ProtectionGroup",
    "AWS::IAM::User",
    "AWS::EMR::InstanceGroupConfig",
    "AWS::StepFunctions::Activity",
    "AWS::Logs::AccountPolicy",
    "AWS::S3::BucketPolicy",
    "AWS::Redshift::Cluster",
    "AWS::EMR::InstanceFleetConfig",
    "AWS::EMR::Cluster",
    "AWS::RDS::DBCluster",
    "AWS::Transfer::Agreement",
    "AWS::CloudFront::Distribution",
    "AWS::ElastiCache::SubnetGroup",
    "AWS::XRay::Group",
    "AWS::Oam::Link",
    "AWS::NetworkFirewall::Firewall",
    "AWS::KMS::ReplicaKey",
    "AWS::Redshift::ClusterSecurityGroup",
    "AWS::ECR::PullThroughCacheRule",
    "AWS::Glue::MLTransform",
    "AWS::AppConfig::HostedConfigurationVersion",
    "AWS::DataSync::LocationEFS",
    "AWS::ApiGateway::Resource",
    "AWS::ElasticLoadBalancingV2::TargetGroup",
    "AWS::ApplicationAutoScaling::ScalingPolicy",
    "AWS::CloudFormation::Macro",
    "AWS::Lambda::LayerVersionPermission",
    "AWS::SecretsManager::Secret",
    "AWS::Route53Resolver::ResolverConfig",
    "AWS::ElastiCache::User",
    "AWS::Logs::SubscriptionFilter",
    "AWS::CodeDeploy::Application",
    "AWS::IoT::TopicRule",
    "AWS::LakeFormation::PrincipalPermissions",
    "AWS::DataSync::LocationS3",
    "AWS::AutoScaling::LifecycleHook",
    "AWS::FSx::DataRepositoryAssociation",
    "AWS::EC2::NetworkInterface",
    "AWS::ControlTower::LandingZone",
    "AWS::RolesAnywhere::TrustAnchor",
    "AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation",
    "AWS::Lambda::EventInvokeConfig",
    "AWS::Lambda::LayerVersion",
    "AWS::RDS::OptionGroup",
    "AWS::OpsWorks::UserProfile",
    "AWS::Logs::Delivery",
    "AWS::IoT::Policy",
    "AWS::EC2::TransitGatewayRoute",
    "AWS::SSM::MaintenanceWindow",
    "AWS::LakeFormation::TagAssociation",
    "AWS::EC2::IPAMResourceDiscovery",
    "AWS::ImageBuilder::InfrastructureConfiguration",
    "AWS::CloudFormation::WaitCondition",
    "AWS::Route53Resolver::ResolverEndpoint",
    "AWS::CloudWatch::AnomalyDetector",
    "AWS::EC2::SubnetNetworkAclAssociation",
    "AWS::DMS::MigrationProject",
    "AWS::IAM::UserPolicy",
    "AWS::CloudFront::OriginAccessControl",
    "AWS::SecretsManager::RotationSchedule",
    "AWS::SecurityHub::SecurityControl",
    "AWS::Lambda::Permission",
    "AWS::NetworkFirewall::FirewallPolicy",
    "AWS::EKS::IdentityProviderConfig",
    "AWS::EC2::IPAMResourceDiscoveryAssociation",
    "AWS::ServiceCatalogAppRegistry::AttributeGroup",
    "AWS::EC2::EgressOnlyInternetGateway",
    "AWS::SecurityHub::Insight",
    "AWS::EC2::VPCCidrBlock",
    "AWS::ACMPCA::CertificateAuthority",
    "AWS::Athena::PreparedStatement",
    "AWS::AutoScaling::ScheduledAction",
    "AWS::LakeFormation::Resource",
    "AWS::EC2::IPAMScope",
    "AWS::DirectoryService::SimpleAD",
    "AWS::EC2::VPCEndpoint",
    "AWS::RDS::EventSubscription",
    "AWS::Config::AggregationAuthorization",
    "AWS::DataSync::Agent",
    "AWS::Logs::LogGroup",
    "AWS::ECS::Cluster",
    "AWS::EC2::TrafficMirrorFilterRule",
    "AWS::EC2::PlacementGroup",
    "AWS::Organizations::Account",
    "AWS::ECR::Repository",
    "AWS::AppConfig::Extension",
    "AWS::ElasticLoadBalancingV2::ListenerRule",
    "AWS::EC2::KeyPair",
    "AWS::FSx::FileSystem",
    "AWS::EC2::EIPAssociation",
    "AWS::ElasticBeanstalk::Application",
    "AWS::IoT::ThingPrincipalAttachment",
    "AWS::DLM::LifecyclePolicy",
    "AWS::EC2::CapacityReservation",
    "AWS::ElasticLoadBalancing::LoadBalancer",
    "AWS::Transfer::User",
    "AWS::IAM::RolePolicy",
    "AWS::EC2::TrafficMirrorTarget",
    "AWS::StepFunctions::StateMachine",
    "AWS::RDS::DBClusterParameterGroup",
    "AWS::WAF::XssMatchSet",
    "AWS::FSx::Snapshot",
    "AWS::Route53::KeySigningKey",
    "AWS::Config::RemediationConfiguration",
    "AWS::Athena::DataCatalog",
    "AWS::Glue::Workflow",
    "AWS::EC2::PrefixList",
    "AWS::EC2::Instance",
    "AWS::EC2::SubnetCidrBlock",
    "AWS::ElasticBeanstalk::ApplicationVersion",
    "AWS::WAF::SqlInjectionMatchSet",
    "AWS::EC2::TransitGatewayVpcAttachment",
    "AWS::EC2::FlowLog",
    "AWS::AmazonMQ::Broker",
    "AWS::EMR::Step",
    "AWS::SSM::Association",
    "AWS::CloudFront::ResponseHeadersPolicy",
    "AWS::SecurityHub::AutomationRule",
    "AWS::MSK::ClusterPolicy",
    "AWS::GuardDuty::Master",
    "AWS::KMS::Alias",
    "AWS::XRay::SamplingRule",
    "AWS::Route53Resolver::ResolverRule",
    "AWS::Transfer::Connector",
    "AWS::ApiGateway::DocumentationVersion",
    "AWS::WAFv2::WebACLAssociation",
    "AWS::Oam::Sink",
    "AWS::ApiGateway::GatewayResponse",
    "AWS::FSx::Volume",
    "AWS::ACMPCA::Certificate",
    "AWS::EC2::IPAMAllocation",
    "AWS::WorkSpaces::Workspace",
    "AWS::DirectoryService::MicrosoftAD",
    "AWS::DataSync::LocationObjectStorage",
    "AWS::ECS::CapacityProvider",
    "AWS::ElastiCache::CacheCluster",
    "AWS::SageMaker::ModelCard",
    "AWS::Logs::Destination",
    "AWS::EKS::Nodegroup",
    "AWS::Organizations::OrganizationalUnit",
    "AWS::SQS::Queue",
    "AWS::EC2::SecurityGroupIngress",
    "AWS::GuardDuty::Detector",
    "AWS::ApiGateway::Stage",
    "AWS::Batch::ComputeEnvironment",
    "AWS::DataPipeline::Pipeline",
    "AWS::IoT::Thing",
    "AWS::Route53::HealthCheck",
    "AWS::Events::EventBusPolicy",
    "AWS::Athena::NamedQuery",
    "AWS::EC2::TrafficMirrorFilter",
    "AWS::ApiGateway::Deployment",
    "AWS::LakeFormation::DataLakeSettings",
    "AWS::AutoScaling::ScalingPolicy",
    "AWS::ResourceExplorer2::DefaultViewAssociation",
    "AWS::ECR::RegistryPolicy",
    "AWS::Redshift::ScheduledAction",
    "AWS::RDS::DBSecurityGroup",
    "AWS::CloudWatch::MetricStream",
    "AWS::DMS::DataProvider",
    "AWS::SSM::Parameter",
    "AWS::Config::DeliveryChannel",
    "AWS::IAM::OIDCProvider",
    "AWS::LakeFormation::Tag",
    "AWS::CE::AnomalyMonitor",
    "AWS::ServiceCatalogAppRegistry::ResourceAssociation",
    "AWS::EC2::VPNGateway",
    "AWS::CloudFormation::Stack",
    "AWS::ResourceGroups::Group",
    "AWS::CloudFormation::ResourceDefaultVersion",
    "AWS::SSM::ResourceDataSync",
    "AWS::EC2::IPAM",
    "AWS::EC2::TransitGatewayPeeringAttachment",
    "AWS::CloudFront::CachePolicy",
    "AWS::IAM::AccessKey",
    "AWS::RDS::DBSubnetGroup",
    "AWS::SecretsManager::SecretTargetAttachment",
    "AWS::AmazonMQ::Configuration",
    "AWS::AppConfig::Deployment",
    "AWS::CodePipeline::CustomActionType",
    "AWS::AccessAnalyzer::Analyzer",
    "AWS::EC2::EC2Fleet",
    "AWS::EC2::VPCEndpointService",
    "AWS::IAM::ManagedPolicy",
    "AWS::EC2::LaunchTemplate",
    "AWS::CloudFront::OriginRequestPolicy",
    "AWS::DataSync::LocationFSxONTAP",
    "AWS::ElasticBeanstalk::Environment",
    "AWS::Lambda::Version",
    "AWS::EC2::DHCPOptions",
    "AWS::EC2::IPAMPool",
    "AWS::Kinesis::StreamConsumer",
    "AWS::IAM::ServiceLinkedRole",
    "AWS::CloudFormation::HookTypeConfig",
    "AWS::EC2::Volume",
    "AWS::IoT::Certificate",
    "AWS::EC2::EIP",
    "AWS::VerifiedPermissions::Policy",
    "AWS::CloudFormation::ResourceVersion",
    "AWS::ApiGatewayV2::Stage",
    "AWS::RDS::DBProxy",
    "AWS::RDS::DBParameterGroup",
    "AWS::SecurityHub::Hub",
    "AWS::S3::AccessPoint",
    "AWS::EC2::TrafficMirrorSession",
    "AWS::Batch::JobQueue",
    "AWS::ElasticLoadBalancingV2::Listener",
    "AWS::Redshift::EventSubscription",
    "AWS::CloudFormation::WaitConditionHandle",
    "AWS::GlobalAccelerator::Accelerator",
    "AWS::EKS::Addon",
]

# pylint: disable=too-many-lines
cached: List[str] = [
    "Module",
    "aws-ce-anomalysubscription.json",
    "aws-shield-drtaccess.json",
    "aws-glue-partition.json",
    "aws-ec2-transitgatewayroutetablepropagation.json",
    "aws-shield-proactiveengagement.json",
    "aws-guardduty-filter.json",
    "aws-ecs-service.json",
    "aws-ram-resourceshare.json",
    "aws-dms-replicationconfig.json",
    "aws-dynamodb-table.json",
    "aws-ec2-securitygroupegress.json",
    "aws-config-organizationconfigrule.json",
    "aws-glue-dataqualityruleset.json",
    "aws-route53profiles-profileassociation.json",
    "aws-config-configurationrecorder.json",
    "aws-cloudfront-continuousdeploymentpolicy.json",
    "aws-ecr-replicationconfiguration.json",
    "aws-appconfig-extensionassociation.json",
    "aws-ec2-ipampoolcidr.json",
    "aws-redshift-clustersubnetgroup.json",
    "aws-ec2-vpcdhcpoptionsassociation.json",
    "aws-ec2-networkacl.json",
    "aws-lambda-eventsourcemapping.json",
    "aws-logs-resourcepolicy.json",
    "aws-dms-instanceprofile.json",
    "aws-transfer-certificate.json",
    "aws-route53profiles-profile.json",
    "aws-cloudwatch-compositealarm.json",
    "aws-route53resolver-firewalldomainlist.json",
    "aws-redshift-endpointaccess.json",
    "aws-appconfig-application.json",
    "aws-datasync-locationfsxwindows.json",
    "aws-autoscaling-warmpool.json",
    "aws-config-storedquery.json",
    "aws-acmpca-permission.json",
    "aws-transfer-server.json",
    "aws-ecs-primarytaskset.json",
    "aws-autoscaling-autoscalinggroup.json",
    "aws-wafv2-regexpatternset.json",
    "aws-eks-fargateprofile.json",
    "aws-route53-dnssec.json",
    "aws-redshift-endpointauthorization.json",
    "aws-ec2-transitgatewayroutetable.json",
    "aws-route53-recordset.json",
    "aws-eks-accessentry.json",
    "aws-elasticache-securitygroup.json",
    "aws-kinesisfirehose-deliverystream.json",
    "aws-imagebuilder-component.json",
    "aws-glue-connection.json",
    "aws-organizations-resourcepolicy.json",
    "aws-ec2-transitgatewaymulticastgroupsource.json",
    "aws-transfer-profile.json",
    "aws-cloudfront-realtimelogconfig.json",
    "aws-lakeformation-datacellsfilter.json",
    "aws-datasync-locationhdfs.json",
    "aws-msk-cluster.json",
    "aws-securityhub-delegatedadmin.json",
    "aws-controltower-enabledbaseline.json",
    "aws-ec2-vpcendpointconnectionnotification.json",
    "aws-codepipeline-pipeline.json",
    "aws-config-configurationaggregator.json",
    "aws-imagebuilder-imagepipeline.json",
    "aws-elasticloadbalancingv2-listenercertificate.json",
    "aws-route53resolver-resolverruleassociation.json",
    "aws-fsx-storagevirtualmachine.json",
    "aws-synthetics-canary.json",
    "aws-sns-subscription.json",
    "aws-ec2-natgateway.json",
    "aws-transfer-workflow.json",
    "aws-appconfig-deploymentstrategy.json",
    "aws-glue-devendpoint.json",
    "aws-elasticache-usergroup.json",
    "aws-logs-deliverydestination.json",
    "aws-imagebuilder-imagerecipe.json",
    "aws-opsworks-elasticloadbalancerattachment.json",
    "aws-s3objectlambda-accesspointpolicy.json",
    "aws-elasticache-replicationgroup.json",
    "aws-stepfunctions-statemachinealias.json",
    "aws-route53profiles-profileresourceassociation.json",
    "aws-glue-job.json",
    "aws-eks-podidentityassociation.json",
    "aws-resourceexplorer2-index.json",
    "aws-glue-table.json",
    "aws-logs-metricfilter.json",
    "aws-lambda-function.json",
    "aws-sns-topic.json",
    "aws-backup-backupselection.json",
    "aws-datasync-locationfsxlustre.json",
    "aws-logs-deliverysource.json",
    "aws-cloudtrail-trail.json",
    "aws-ec2-internetgateway.json",
    "aws-ec2-gatewayroutetableassociation.json",
    "aws-wafv2-ipset.json",
    "aws-ssm-document.json",
    "aws-elasticache-serverlesscache.json",
    "aws-cloudfront-cloudfrontoriginaccessidentity.json",
    "aws-kinesisanalyticsv2-application.json",
    "aws-lambda-alias.json",
    "aws-ec2-transitgatewaymulticastdomainassociation.json",
    "aws-ec2-transitgatewayroutetableassociation.json",
    "aws-appconfig-environment.json",
    "aws-imagebuilder-image.json",
    "aws-elasticache-securitygroupingress.json",
    "aws-rds-dbproxytargetgroup.json",
    "aws-cloudwatch-dashboard.json",
    "aws-cloudwatch-alarm.json",
    "aws-guardduty-member.json",
    "aws-cloudformation-customresource.json",
    "aws-wafv2-rulegroup.json",
    "aws-networkfirewall-loggingconfiguration.json",
    "aws-glue-classifier.json",
    "aws-codedeploy-deploymentgroup.json",
    "aws-cloudformation-stackset.json",
    "aws-ec2-route.json",
    "aws-cloudformation-hookversion.json",
    "aws-rolesanywhere-profile.json",
    "aws-xray-resourcepolicy.json",
    "aws-wafv2-loggingconfiguration.json",
    "aws-dynamodb-globaltable.json",
    "aws-backup-backupplan.json",
    "aws-imagebuilder-distributionconfiguration.json",
    "aws-lakeformation-permissions.json",
    "aws-resourceexplorer2-view.json",
    "aws-glue-datacatalogencryptionsettings.json",
    "aws-cloudfront-publickey.json",
    "aws-identitystore-group.json",
    "aws-ram-permission.json",
    "aws-datasync-task.json",
    "aws-ecs-taskdefinition.json",
    "aws-shield-protection.json",
    "aws-identitystore-groupmembership.json",
    "aws-ec2-spotfleet.json",
    "aws-msk-batchscramsecret.json",
    "aws-s3-bucket.json",
    "aws-guardduty-ipset.json",
    "aws-servicediscovery-httpnamespace.json",
    "aws-cloudwatch-insightrule.json",
    "aws-batch-schedulingpolicy.json",
    "aws-athena-workgroup.json",
    "aws-iam-servercertificate.json",
    "aws-globalaccelerator-crossaccountattachment.json",
    "aws-sqs-queueinlinepolicy.json",
    "aws-organizations-organization.json",
    "aws-ssm-maintenancewindowtarget.json",
    "aws-rds-dbsecuritygroupingress.json",
    "aws-securityhub-organizationconfiguration.json",
    "aws-glue-securityconfiguration.json",
    "aws-networkfirewall-tlsinspectionconfiguration.json",
    "aws-ecs-clustercapacityproviderassociations.json",
    "aws-appconfig-configurationprofile.json",
    "aws-msk-configuration.json",
    "aws-ec2-transitgateway.json",
    "aws-ec2-vpcendpointservicepermissions.json",
    "aws-ssm-maintenancewindowtask.json",
    "aws-ec2-transitgatewaymulticastdomain.json",
    "aws-verifiedpermissions-policytemplate.json",
    "aws-efs-filesystem.json",
    "aws-logs-querydefinition.json",
    "aws-securityhub-productsubscription.json",
    "aws-datasync-locationnfs.json",
    "aws-certificatemanager-certificate.json",
    "aws-sdb-domain.json",
    "aws-ec2-subnetroutetableassociation.json",
    "aws-imagebuilder-containerrecipe.json",
    "aws-efs-accesspoint.json",
    "aws-redshift-clustersecuritygroupingress.json",
    "aws-servicecatalogappregistry-attributegroupassociation.json",
    "aws-elasticloadbalancingv2-loadbalancer.json",
    "aws-opensearchservice-domain.json",
    "aws-servicediscovery-instance.json",
    "aws-elasticsearch-domain.json",
    "aws-servicediscovery-privatednsnamespace.json",
    "aws-secretsmanager-resourcepolicy.json",
    "aws-cloudformation-hookdefaultversion.json",
    "aws-imagebuilder-workflow.json",
    "aws-ecs-taskset.json",
    "aws-acmpca-certificateauthorityactivation.json",
    "aws-guardduty-threatintelset.json",
    "aws-ec2-vpc.json",
    "aws-arczonalshift-zonalautoshiftconfiguration.json",
    "aws-msk-vpcconnection.json",
    "aws-datasync-locationazureblob.json",
    "aws-logs-logstream.json",
    "aws-route53-recordsetgroup.json",
    "aws-cloudformation-publictypeversion.json",
    "aws-opsworks-app.json",
    "aws-kinesis-stream.json",
    "aws-iam-samlprovider.json",
    "aws-cloudfront-keygroup.json",
    "aws-ec2-networkinterfaceattachment.json",
    "aws-glue-customentitytype.json",
    "aws-codedeploy-deploymentconfig.json",
    "aws-stepfunctions-statemachineversion.json",
    "aws-servicecatalogappregistry-application.json",
    "aws-glue-database.json",
    "aws-backup-backupvault.json",
    "aws-ec2-customergateway.json",
    "aws-iam-grouppolicy.json",
    "aws-waf-bytematchset.json",
    "aws-ec2-routetable.json",
    "aws-rds-dbproxyendpoint.json",
    "aws-datasync-locationsmb.json",
    "aws-securityhub-standard.json",
    "aws-rolesanywhere-crl.json",
    "aws-sns-topicinlinepolicy.json",
    "aws-redshift-clusterparametergroup.json",
    "aws-organizations-policy.json",
    "aws-glue-trigger.json",
    "aws-globalaccelerator-listener.json",
    "aws-verifiedpermissions-policystore.json",
    "aws-ec2-vpcpeeringconnection.json",
    "aws-sns-topicpolicy.json",
    "aws-networkfirewall-rulegroup.json",
    "aws-datasync-locationfsxopenzfs.json",
    "aws-kms-key.json",
    "aws-route53resolver-resolverdnssecconfig.json",
    "aws-route53resolver-firewallrulegroupassociation.json",
    "aws-route53resolver-resolverqueryloggingconfig.json",
    "aws-ec2-snapshotblockpublicaccess.json",
    "aws-ec2-subnet.json",
    "aws-s3objectlambda-accesspoint.json",
    "aws-sqs-queuepolicy.json",
    "aws-wafv2-webacl.json",
    "aws-globalaccelerator-endpointgroup.json",
    "aws-ec2-capacityreservationfleet.json",
    "aws-opsworks-volume.json",
    "aws-iam-usertogroupaddition.json",
    "aws-events-rule.json",
    "aws-cloudfront-keyvaluestore.json",
    "aws-guardduty-malwareprotectionplan.json",
    "aws-glue-crawler.json",
    "aws-cloudfront-function.json",
    "aws-ssm-patchbaseline.json",
    "aws-servicediscovery-service.json",
    "aws-cloudfront-monitoringsubscription.json",
    "aws-efs-mounttarget.json",
    "aws-servicediscovery-publicdnsnamespace.json",
    "aws-shield-protectiongroup.json",
    "aws-emr-instancegroupconfig.json",
    "aws-stepfunctions-activity.json",
    "aws-logs-accountpolicy.json",
    "aws-s3-bucketpolicy.json",
    "aws-redshift-cluster.json",
    "aws-emr-instancefleetconfig.json",
    "aws-emr-cluster.json",
    "aws-transfer-agreement.json",
    "aws-cloudfront-distribution.json",
    "aws-xray-group.json",
    "aws-oam-link.json",
    "aws-networkfirewall-firewall.json",
    "aws-kms-replicakey.json",
    "aws-redshift-clustersecuritygroup.json",
    "aws-ecr-pullthroughcacherule.json",
    "aws-glue-mltransform.json",
    "aws-appconfig-hostedconfigurationversion.json",
    "aws-datasync-locationefs.json",
    "aws-elasticloadbalancingv2-targetgroup.json",
    "aws-cloudformation-macro.json",
    "aws-lambda-layerversionpermission.json",
    "aws-secretsmanager-secret.json",
    "aws-route53resolver-resolverconfig.json",
    "aws-elasticache-user.json",
    "aws-logs-subscriptionfilter.json",
    "aws-codedeploy-application.json",
    "aws-lakeformation-principalpermissions.json",
    "aws-datasync-locations3.json",
    "aws-fsx-datarepositoryassociation.json",
    "aws-ec2-networkinterface.json",
    "aws-controltower-landingzone.json",
    "aws-rolesanywhere-trustanchor.json",
    "aws-route53resolver-resolverqueryloggingconfigassociation.json",
    "aws-lambda-eventinvokeconfig.json",
    "aws-lambda-layerversion.json",
    "aws-rds-optiongroup.json",
    "aws-opsworks-userprofile.json",
    "aws-logs-delivery.json",
    "aws-ec2-transitgatewayroute.json",
    "aws-ssm-maintenancewindow.json",
    "aws-lakeformation-tagassociation.json",
    "aws-ec2-ipamresourcediscovery.json",
    "aws-imagebuilder-infrastructureconfiguration.json",
    "aws-route53resolver-resolverendpoint.json",
    "aws-cloudwatch-anomalydetector.json",
    "aws-dms-migrationproject.json",
    "aws-iam-userpolicy.json",
    "aws-cloudfront-originaccesscontrol.json",
    "aws-secretsmanager-rotationschedule.json",
    "aws-securityhub-securitycontrol.json",
    "aws-lambda-permission.json",
    "aws-networkfirewall-firewallpolicy.json",
    "aws-eks-identityproviderconfig.json",
    "aws-ec2-ipamresourcediscoveryassociation.json",
    "aws-servicecatalogappregistry-attributegroup.json",
    "aws-ec2-egressonlyinternetgateway.json",
    "aws-securityhub-insight.json",
    "aws-ec2-vpccidrblock.json",
    "aws-acmpca-certificateauthority.json",
    "aws-athena-preparedstatement.json",
    "aws-lakeformation-resource.json",
    "aws-ec2-ipamscope.json",
    "aws-rds-eventsubscription.json",
    "module.json",
    "aws-config-aggregationauthorization.json",
    "aws-datasync-agent.json",
    "aws-logs-loggroup.json",
    "aws-ec2-placementgroup.json",
    "aws-organizations-account.json",
    "aws-ecr-repository.json",
    "aws-appconfig-extension.json",
    "aws-elasticloadbalancingv2-listenerrule.json",
    "aws-ec2-keypair.json",
    "aws-fsx-filesystem.json",
    "aws-ec2-eipassociation.json",
    "aws-dlm-lifecyclepolicy.json",
    "aws-ec2-capacityreservation.json",
    "aws-elasticloadbalancing-loadbalancer.json",
    "aws-transfer-user.json",
    "aws-iam-rolepolicy.json",
    "aws-ec2-trafficmirrortarget.json",
    "aws-stepfunctions-statemachine.json",
    "aws-rds-dbclusterparametergroup.json",
    "aws-fsx-snapshot.json",
    "aws-route53-keysigningkey.json",
    "aws-config-remediationconfiguration.json",
    "aws-athena-datacatalog.json",
    "aws-glue-workflow.json",
    "aws-ec2-prefixlist.json",
    "aws-ec2-instance.json",
    "aws-waf-sqlinjectionmatchset.json",
    "aws-ec2-transitgatewayvpcattachment.json",
    "aws-ec2-flowlog.json",
    "aws-amazonmq-broker.json",
    "aws-ssm-association.json",
    "aws-cloudfront-responseheaderspolicy.json",
    "aws-securityhub-automationrule.json",
    "aws-msk-clusterpolicy.json",
    "aws-guardduty-master.json",
    "aws-kms-alias.json",
    "aws-xray-samplingrule.json",
    "aws-route53resolver-resolverrule.json",
    "aws-transfer-connector.json",
    "aws-wafv2-webaclassociation.json",
    "aws-oam-sink.json",
    "aws-fsx-volume.json",
    "aws-acmpca-certificate.json",
    "aws-ec2-ipamallocation.json",
    "aws-workspaces-workspace.json",
    "aws-datasync-locationobjectstorage.json",
    "aws-ecs-capacityprovider.json",
    "aws-elasticache-cachecluster.json",
    "aws-sagemaker-modelcard.json",
    "aws-logs-destination.json",
    "aws-eks-nodegroup.json",
    "aws-organizations-organizationalunit.json",
    "aws-sqs-queue.json",
    "aws-ec2-securitygroupingress.json",
    "aws-guardduty-detector.json",
    "aws-batch-computeenvironment.json",
    "aws-events-eventbuspolicy.json",
    "aws-athena-namedquery.json",
    "aws-ec2-trafficmirrorfilter.json",
    "aws-lakeformation-datalakesettings.json",
    "aws-resourceexplorer2-defaultviewassociation.json",
    "aws-ecr-registrypolicy.json",
    "aws-redshift-scheduledaction.json",
    "aws-rds-dbsecuritygroup.json",
    "aws-cloudwatch-metricstream.json",
    "aws-dms-dataprovider.json",
    "aws-ssm-parameter.json",
    "aws-config-deliverychannel.json",
    "aws-iam-oidcprovider.json",
    "aws-lakeformation-tag.json",
    "aws-ce-anomalymonitor.json",
    "aws-servicecatalogappregistry-resourceassociation.json",
    "aws-ec2-vpngateway.json",
    "aws-resourcegroups-group.json",
    "aws-cloudformation-resourcedefaultversion.json",
    "aws-ssm-resourcedatasync.json",
    "aws-ec2-ipam.json",
    "aws-ec2-transitgatewaypeeringattachment.json",
    "aws-cloudfront-cachepolicy.json",
    "aws-rds-dbsubnetgroup.json",
    "aws-amazonmq-configuration.json",
    "aws-appconfig-deployment.json",
    "aws-accessanalyzer-analyzer.json",
    "aws-ec2-ec2fleet.json",
    "aws-ec2-vpcendpointservice.json",
    "aws-iam-managedpolicy.json",
    "aws-ec2-launchtemplate.json",
    "aws-cloudfront-originrequestpolicy.json",
    "aws-datasync-locationfsxontap.json",
    "aws-lambda-version.json",
    "aws-ec2-dhcpoptions.json",
    "aws-ec2-ipampool.json",
    "aws-iam-servicelinkedrole.json",
    "aws-cloudformation-hooktypeconfig.json",
    "aws-ec2-eip.json",
    "aws-verifiedpermissions-policy.json",
    "aws-cloudformation-resourceversion.json",
    "aws-apigatewayv2-stage.json",
    "aws-rds-dbproxy.json",
    "aws-rds-dbparametergroup.json",
    "aws-securityhub-hub.json",
    "aws-s3-accesspoint.json",
    "aws-batch-jobqueue.json",
    "aws-elasticloadbalancingv2-listener.json",
    "aws-redshift-eventsubscription.json",
    "aws-cloudformation-waitconditionhandle.json",
    "aws-globalaccelerator-accelerator.json",
    "aws-eks-addon.json",
]
