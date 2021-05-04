# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Academicexperiecemodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    institutionname = models.TextField(db_column='InstitutionName', blank=True, null=True)  # Field name made lowercase.
    institutionaddress = models.TextField(db_column='InstitutionAddress', blank=True, null=True)  # Field name made lowercase.
    programmestudied = models.TextField(db_column='ProgrammeStudied', blank=True, null=True)  # Field name made lowercase.
    from_field = models.DateTimeField(db_column='From')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    to = models.DateTimeField(db_column='To')  # Field name made lowercase.
    grade = models.TextField(db_column='Grade', blank=True, null=True)  # Field name made lowercase.
    applicantmodelid = models.IntegerField(db_column='ApplicantModelID', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AcademicExperieceModel'


class Applicantissuemodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    applicantmodelid = models.IntegerField(db_column='ApplicantModelID')  # Field name made lowercase.
    results = models.BooleanField(db_column='Results')  # Field name made lowercase.
    picture = models.BooleanField(db_column='Picture')  # Field name made lowercase.
    age = models.BooleanField(db_column='Age')  # Field name made lowercase.
    formcompletion = models.BooleanField(db_column='FormCompletion')  # Field name made lowercase.
    qualification = models.BooleanField(db_column='Qualification')  # Field name made lowercase.
    issuesone = models.TextField(db_column='IssuesOne', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ApplicantIssueModel'


class Applicantmodel(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    applicationnumber = models.IntegerField(db_column='ApplicationNumber')  # Field name made lowercase.
    title = models.TextField(db_column='Title')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    middlename = models.TextField(db_column='MiddleName', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    previousname = models.TextField(db_column='PreviousName', blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateTimeField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    gender = models.TextField(db_column='Gender')  # Field name made lowercase.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    maritalstatus = models.TextField(db_column='MaritalStatus')  # Field name made lowercase.
    phone = models.TextField(db_column='Phone')  # Field name made lowercase.
    altphone = models.TextField(db_column='AltPhone', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email')  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    postgprs = models.TextField(db_column='PostGPRS', blank=True, null=True)  # Field name made lowercase.
    emergencycontact = models.TextField(db_column='EmergencyContact', blank=True, null=True)  # Field name made lowercase.
    hometown = models.TextField(db_column='Hometown', blank=True, null=True)  # Field name made lowercase.
    nationalidtype = models.TextField(db_column='NationalIDType', blank=True, null=True)  # Field name made lowercase.
    nationalidno = models.TextField(db_column='NationalIDNo', blank=True, null=True)  # Field name made lowercase.
    residentialstatus = models.BooleanField(db_column='ResidentialStatus', blank=True, null=True)  # Field name made lowercase.
    guardianname = models.TextField(db_column='GuardianName', blank=True, null=True)  # Field name made lowercase.
    guardianphone = models.TextField(db_column='GuardianPhone', blank=True, null=True)  # Field name made lowercase.
    guardianoccupation = models.TextField(db_column='GuardianOccupation', blank=True, null=True)  # Field name made lowercase.
    guardianrelationship = models.TextField(db_column='GuardianRelationship', blank=True, null=True)  # Field name made lowercase.
    disability = models.BooleanField(db_column='Disability', blank=True, null=True)  # Field name made lowercase.
    disabilitytype = models.TextField(db_column='DisabilityType', blank=True, null=True)  # Field name made lowercase.
    sourceoffinance = models.TextField(db_column='SourceOfFinance', blank=True, null=True)  # Field name made lowercase.
    applicationuserid1 = models.OneToOneField('Aspnetusers', models.DO_NOTHING, db_column='ApplicationUserId1', blank=True, null=True)  # Field name made lowercase.
    denomination = models.TextField(db_column='Denomination', blank=True, null=True)  # Field name made lowercase.
    referrals = models.TextField(db_column='Referrals', blank=True, null=True)  # Field name made lowercase.
    entrymode = models.TextField(db_column='EntryMode', blank=True, null=True)  # Field name made lowercase.
    firstqualification = models.TextField(db_column='FirstQualification', blank=True, null=True)  # Field name made lowercase.
    secondqualification = models.TextField(db_column='SecondQualification', blank=True, null=True)  # Field name made lowercase.
    programmestudied = models.TextField(db_column='ProgrammeStudied', blank=True, null=True)  # Field name made lowercase.
    formerschool = models.TextField(db_column='FormerSchool', blank=True, null=True)  # Field name made lowercase.
    lastyearinschool = models.IntegerField(db_column='LastYearInSchool')  # Field name made lowercase.
    awaiting = models.BooleanField(db_column='Awaiting', blank=True, null=True)  # Field name made lowercase.
    grade = models.IntegerField(db_column='Grade')  # Field name made lowercase.
    yearofadmission = models.TextField(db_column='YearOfAdmission', blank=True, null=True)  # Field name made lowercase.
    preferedhall = models.TextField(db_column='PreferedHall', blank=True, null=True)  # Field name made lowercase.
    results = models.TextField(db_column='Results', blank=True, null=True)  # Field name made lowercase.
    externalhostel = models.TextField(db_column='ExternalHostel', blank=True, null=True)  # Field name made lowercase.
    elligible = models.BooleanField(db_column='Elligible', blank=True, null=True)  # Field name made lowercase.
    admitted = models.BooleanField(db_column='Admitted', blank=True, null=True)  # Field name made lowercase.
    admittedby = models.IntegerField(db_column='AdmittedBy')  # Field name made lowercase.
    dateadmitted = models.DateTimeField(db_column='DateAdmitted')  # Field name made lowercase.
    admissiontype = models.TextField(db_column='AdmissionType', blank=True, null=True)  # Field name made lowercase.
    sectionadmitted = models.TextField(db_column='SectionAdmitted', blank=True, null=True)  # Field name made lowercase.
    halladmitted = models.TextField(db_column='HallAdmitted', blank=True, null=True)  # Field name made lowercase.
    roomno = models.TextField(db_column='RoomNo', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    smssent = models.BooleanField(db_column='SMSSent', blank=True, null=True)  # Field name made lowercase.
    letterprinted = models.BooleanField(db_column='LetterPrinted', blank=True, null=True)  # Field name made lowercase.
    feepaying = models.BooleanField(db_column='FeePaying', blank=True, null=True)  # Field name made lowercase.
    reportedinschool = models.BooleanField(db_column='ReportedInSchool', blank=True, null=True)  # Field name made lowercase.
    feespaid = models.DecimalField(db_column='FeesPaid', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    reported = models.BooleanField(db_column='Reported')  # Field name made lowercase.
    sponsorship = models.BooleanField(db_column='SponsorShip', blank=True, null=True)  # Field name made lowercase.
    sponsorshipcompany = models.TextField(db_column='SponsorShipCompany', blank=True, null=True)  # Field name made lowercase.
    sponsorshiplocation = models.TextField(db_column='SponsorShipLocation', blank=True, null=True)  # Field name made lowercase.
    sponsorshipcompanycontact = models.TextField(db_column='SponsorShipCompanyContact', blank=True, null=True)  # Field name made lowercase.
    districtid = models.ForeignKey('Districtmodel', models.DO_NOTHING, db_column='DistrictId', blank=True, null=True)  # Field name made lowercase.
    firstchoiceid = models.IntegerField(db_column='FirstChoiceId')  # Field name made lowercase.
    nationalityid = models.ForeignKey('Countrymodel', models.DO_NOTHING, db_column='NationalityId')  # Field name made lowercase.
    secondchoiceid = models.IntegerField(db_column='SecondChoiceId')  # Field name made lowercase.
    thirdchoiceid = models.IntegerField(db_column='ThirdChoiceId')  # Field name made lowercase.
    regionid = models.ForeignKey('Regionmodel', models.DO_NOTHING, db_column='RegionId', blank=True, null=True)  # Field name made lowercase.
    religionid = models.ForeignKey('Religionmodel', models.DO_NOTHING, db_column='ReligionId')  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn')  # Field name made lowercase.
    hallid = models.ForeignKey('Hallmodel', models.DO_NOTHING, db_column='HallId', blank=True, null=True)  # Field name made lowercase.
    applicationuserid = models.TextField(db_column='ApplicationUserId', blank=True, null=True)  # Field name made lowercase.
    formerschoolnewid = models.ForeignKey('Formerschoolmodel', models.DO_NOTHING, db_column='FormerSchoolNewId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ApplicantModel'


class Applicantmodelprogrammemodel(models.Model):
    applicantid = models.IntegerField(db_column='ApplicantID', primary_key=True)  # Field name made lowercase.
    programmesid = models.ForeignKey('Programmemodel', models.DO_NOTHING, db_column='ProgrammesId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ApplicantModelProgrammeModel'
        unique_together = (('applicantid', 'programmesid'),)


class Aspnetroleclaims(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    roleid = models.ForeignKey('Aspnetroles', models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.
    claimtype = models.TextField(db_column='ClaimType', blank=True, null=True)  # Field name made lowercase.
    claimvalue = models.TextField(db_column='ClaimValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetRoleClaims'


class Aspnetroles(models.Model):
    id = models.TextField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    normalizedname = models.TextField(db_column='NormalizedName', unique=True, blank=True, null=True)  # Field name made lowercase.
    concurrencystamp = models.TextField(db_column='ConcurrencyStamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetRoles'


class Aspnetuserclaims(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Aspnetusers', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    claimtype = models.TextField(db_column='ClaimType', blank=True, null=True)  # Field name made lowercase.
    claimvalue = models.TextField(db_column='ClaimValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUserClaims'


class Aspnetuserlogins(models.Model):
    loginprovider = models.TextField(db_column='LoginProvider', primary_key=True)  # Field name made lowercase.
    providerkey = models.TextField(db_column='ProviderKey')  # Field name made lowercase.
    providerdisplayname = models.TextField(db_column='ProviderDisplayName', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Aspnetusers', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUserLogins'
        unique_together = (('loginprovider', 'providerkey'),)


class Aspnetuserroles(models.Model):
    userid = models.OneToOneField('Aspnetusers', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase.
    roleid = models.ForeignKey(Aspnetroles, models.DO_NOTHING, db_column='RoleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUserRoles'
        unique_together = (('userid', 'roleid'),)


class Aspnetusertokens(models.Model):
    userid = models.OneToOneField('Aspnetusers', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase.
    loginprovider = models.TextField(db_column='LoginProvider')  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUserTokens'
        unique_together = (('userid', 'loginprovider', 'name'),)


class Aspnetusers(models.Model):
    id = models.TextField(db_column='Id', primary_key=True)  # Field name made lowercase.
    username = models.TextField(db_column='UserName', blank=True, null=True)  # Field name made lowercase.
    normalizedusername = models.TextField(db_column='NormalizedUserName', unique=True, blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    normalizedemail = models.TextField(db_column='NormalizedEmail', blank=True, null=True)  # Field name made lowercase.
    passwordhash = models.TextField(db_column='PasswordHash', blank=True, null=True)  # Field name made lowercase.
    securitystamp = models.TextField(db_column='SecurityStamp', blank=True, null=True)  # Field name made lowercase.
    concurrencystamp = models.TextField(db_column='ConcurrencyStamp', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.TextField(db_column='PhoneNumber', blank=True, null=True)  # Field name made lowercase.
    lockoutend = models.TextField(db_column='LockoutEnd', blank=True, null=True)  # Field name made lowercase.
    accessfailedcount = models.IntegerField(db_column='AccessFailedCount')  # Field name made lowercase.
    emailconfirmed = models.BooleanField(db_column='EmailConfirmed')  # Field name made lowercase.
    lockoutenabled = models.BooleanField(db_column='LockoutEnabled')  # Field name made lowercase.
    phonenumberconfirmed = models.BooleanField(db_column='PhoneNumberConfirmed')  # Field name made lowercase.
    twofactorenabled = models.BooleanField(db_column='TwoFactorEnabled')  # Field name made lowercase.
    branch = models.TextField(db_column='Branch', blank=True, null=True)  # Field name made lowercase.
    finalized = models.IntegerField(db_column='Finalized')  # Field name made lowercase.
    formcompleted = models.IntegerField(db_column='FormCompleted')  # Field name made lowercase.
    formno = models.TextField(db_column='FormNo', blank=True, null=True)  # Field name made lowercase.
    fullname = models.TextField(db_column='FullName', blank=True, null=True)  # Field name made lowercase.
    pictureuploaded = models.IntegerField(db_column='PictureUploaded')  # Field name made lowercase.
    pin = models.TextField(db_column='Pin', blank=True, null=True)  # Field name made lowercase.
    sold = models.IntegerField(db_column='Sold')  # Field name made lowercase.
    soldby = models.TextField(db_column='SoldBy', blank=True, null=True)  # Field name made lowercase.
    started = models.IntegerField(db_column='Started')  # Field name made lowercase.
    teller = models.TextField(db_column='Teller', blank=True, null=True)  # Field name made lowercase.
    tellerphone = models.TextField(db_column='TellerPhone', blank=True, null=True)  # Field name made lowercase.
    year = models.TextField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    lastlogin = models.DateTimeField(db_column='LastLogin')  # Field name made lowercase.
    admitted = models.BooleanField(db_column='Admitted')  # Field name made lowercase.
    resultuploaded = models.BooleanField(db_column='ResultUploaded')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AspNetUsers'


class Bankmodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    account = models.TextField(db_column='Account', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BankModel'


class Countrymodel(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CountryModel'


class Denominationmodel(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DenominationModel'


class Departmentmodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    faculty = models.IntegerField(db_column='Faculty')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepartmentModel'


class Districtmodel(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    region = models.IntegerField(db_column='Region')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DistrictModel'


class Documentuploadmodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    applicant = models.IntegerField(db_column='Applicant')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    applicantmodelid = models.IntegerField(db_column='ApplicantModelID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DocumentUploadModel'


class Exammodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    cutoffpoint = models.TextField(db_column='CutOffPoint', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExamModel'


class Facultymodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FacultyModel'


class Formnomodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    no = models.IntegerField(db_column='No')  # Field name made lowercase.
    year = models.TextField(db_column='Year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FormNoModel'


class Formerschoolmodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    region = models.IntegerField(db_column='Region')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FormerSchoolModel'


class Grademodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    exam = models.IntegerField(db_column='Exam')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GradeModel'


class Hallmodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    bankacc = models.IntegerField(db_column='BankAcc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HallModel'


class Programmemodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    leveladmitted = models.TextField(db_column='LevelAdmitted', blank=True, null=True)  # Field name made lowercase.
    runing = models.BooleanField(db_column='Runing', blank=True, null=True)  # Field name made lowercase.
    showonportal = models.BooleanField(db_column='ShowOnPortal', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration')  # Field name made lowercase.
    department = models.IntegerField(db_column='Department')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProgrammeModel'


class Regionmodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RegionModel'


class Religionmodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReligionModel'


class Requirementmodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    department = models.IntegerField(db_column='Department')  # Field name made lowercase.
    year = models.TextField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    aprroved = models.BooleanField(db_column='Aprroved')  # Field name made lowercase.
    ruleone = models.TextField(db_column='RuleOne', blank=True, null=True)  # Field name made lowercase.
    ruletwo = models.TextField(db_column='RuleTwo', blank=True, null=True)  # Field name made lowercase.
    rulethree = models.TextField(db_column='RuleThree', blank=True, null=True)  # Field name made lowercase.
    applicantmodelid = models.IntegerField(db_column='ApplicantModelID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RequirementModel'


class Resultuploadmodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    applicant = models.IntegerField(db_column='Applicant')  # Field name made lowercase.
    examtype = models.TextField(db_column='ExamType', blank=True, null=True)  # Field name made lowercase.
    gradeold = models.IntegerField(db_column='GradeOld')  # Field name made lowercase.
    gradevalueold = models.TextField(db_column='GradeValueOld', blank=True, null=True)  # Field name made lowercase.
    indexno = models.TextField(db_column='IndexNo', blank=True, null=True)  # Field name made lowercase.
    sitting = models.TextField(db_column='Sitting', blank=True, null=True)  # Field name made lowercase.
    month = models.TextField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    form = models.TextField(db_column='Form', blank=True, null=True)  # Field name made lowercase.
    center = models.TextField(db_column='Center', blank=True, null=True)  # Field name made lowercase.
    year = models.TextField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    oldsubject = models.TextField(db_column='OldSubject', blank=True, null=True)  # Field name made lowercase.
    institutionname = models.TextField(db_column='InstitutionName', blank=True, null=True)  # Field name made lowercase.
    applicantmodelid = models.IntegerField(db_column='ApplicantModelID')  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn')  # Field name made lowercase.
    gradeid = models.ForeignKey(Grademodel, models.DO_NOTHING, db_column='GradeId', blank=True, null=True)  # Field name made lowercase.
    subjectid = models.ForeignKey('Subjectmodel', models.DO_NOTHING, db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResultUploadModel'
        unique_together = (('indexno', 'sitting', 'subjectid', 'gradeid', 'year', 'month', 'examtype'),)


class Shsprogrammes(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SHSProgrammes'


class Smsmodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    message = models.TextField(db_column='Message', blank=True, null=True)  # Field name made lowercase.
    sentby = models.IntegerField(db_column='SentBy')  # Field name made lowercase.
    recipient = models.IntegerField(db_column='Recipient')  # Field name made lowercase.
    datesent = models.DateTimeField(db_column='DateSent')  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    applicantmodelid = models.IntegerField(db_column='ApplicantModelID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMSModel'


class Schoolmodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SchoolModel'


class Subjectmodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubjectModel'


class Workingexperiencemodel(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
    companyphone = models.TextField(db_column='CompanyPhone', blank=True, null=True)  # Field name made lowercase.
    companyaddress = models.TextField(db_column='CompanyAddress', blank=True, null=True)  # Field name made lowercase.
    companyposition = models.TextField(db_column='CompanyPosition', blank=True, null=True)  # Field name made lowercase.
    companyfrom = models.TextField(db_column='CompanyFrom', blank=True, null=True)  # Field name made lowercase.
    companyto = models.TextField(db_column='CompanyTo', blank=True, null=True)  # Field name made lowercase.
    applicantmodelid = models.IntegerField(db_column='ApplicantModelID', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkingExperienceModel'


class Efmigrationshistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__EFMigrationsHistory'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
