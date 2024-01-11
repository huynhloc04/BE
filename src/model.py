from datetime import datetime
from sqlalchemy import text, Column, TIMESTAMP
from sqlmodel import Field, SQLModel, Relationship, JSON
from typing import List, Optional, Set
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.dialects import postgresql
from enum import Enum
from sqlalchemy.types import Integer, String


class TableBase(SQLModel):
    """
    A base class for SQLModel tables.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
        ),
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
            onupdate=datetime.utcnow,
        )
    )


class User(TableBase, table=True):
    __tablename__ = 'users'

    fullname: str = Field(default=None)
    email: str = Field(default=None)
    phone: str = Field(default=None)
    role: str = Field(default=None)
    point: float = Field(default=0)
    avatar: str = Field(default=None)
    country: str = Field(default=None)
    city: str = Field(default=None)
    address: str = Field(default=None, sa_column=Column(TEXT))
    password: str = Field(default=None)
    last_signed_in: datetime = Field(default=None)
    refresh_token: str = Field(max_length=255, nullable=True)
    otp_token: str = Field(default=None)
    is_verify: Optional[bool] = Field(default=False)
    is_active: Optional[bool] = Field(default=False)
    is_verify_forgot_password: Optional[bool] = Field(default=False)


class JWTModel(TableBase, table=True): # BlacklistToken
    __tablename__ = "blacklisted_jwt"
    
    token: str = Field(unique=True, nullable=False)


class Company(TableBase, table=True):
    __tablename__ = 'companies'
    
    user_id: int = Field(default=None, foreign_key="users.id")
    company_name: str = Field(default=None)
    industry: str = Field(default=None)
    phone: str = Field(default=None)
    email: str = Field(default=None)
    description: str = Field(default=None, sa_column=Column(TEXT))
    founded_year: int = Field(default=None)
    company_size: int = Field(default=None)
    tax_code: str = Field(default=None)    
    address: str = Field(default=None, sa_column=Column(TEXT))
    city: str = Field(default=None)
    country: str = Field(default=None)    
    logo: str = Field(default=None)
    cover_image: Optional[str] = Field(default=None)
    company_images: Optional[List[str]] = Field(default=None, sa_column=Column(postgresql.ARRAY(String())))
    company_video: Optional[str] = Field(default=None)
    linkedin: Optional[str] = Field(default=None)
    website: Optional[str] = Field(default=None)
    facebook: Optional[str] = Field(default=None)
    instagram: Optional[str] = Field(default=None)


class JobDescription(TableBase, table=True):
    __tablename__ = 'job_descriptions'

    user_id: int = Field(default=None, foreign_key="users.id")
    status: str = Field(default=None)
    job_service: str = Field(default=None)
    job_title: str = Field(default=None)
    industries: List[str] = Field(default=None, sa_column=Column(postgresql.ARRAY(String())))
    gender: Optional[str] = Field(default=None)
    job_type: str = Field(default=None)
    skills: List[str] = Field(default=None, sa_column=Column(postgresql.ARRAY(String())))
    received_job_time: datetime = Field(default=None)
    working_time: str = Field(default=None)
    description: str = Field(default=None)
    requirement: str = Field(default=None)
    benefits: List[str] = Field(default=None, sa_column=Column(postgresql.ARRAY(String())))
    levels: List[str] = Field(default=None, sa_column=Column(postgresql.ARRAY(String())))
    roles: List[str] = Field(default=None, sa_column=Column(postgresql.ARRAY(String())))
    yoe: int = Field(default=None)
    num_recruit: int = Field(default=None)
    min_salary: float = Field(default=None)
    max_salary: float = Field(default=None)
    currency: str = Field(default=None)
    address: str = Field(default=None)
    city: str = Field(default=None)
    country: str = Field(default=None)
    point: float = Field(default=None)
    jd_file: str = Field(default=None)
    status: str = Field(default="pending")
    is_favorite: bool = Field(default=False)
    is_draft: bool = Field(default=False)
    is_admin_approved: bool = Field(default=False)      # Admin filtered Job
    admin_decline_reason: str = Field(default=None, sa_column=Column(TEXT))
    company_decline_reason: str = Field(default=None, sa_column=Column(TEXT))
    
class JobEducation(TableBase, table=True):
    __tablename__ = 'job_educations'    
    job_id: int = Field(default=None, foreign_key="job_descriptions.id")
    degree: str = Field(default=None)
    major: str = Field(default=None)
    gpa: float = Field(default=None)
    
class LanguageCertificate(TableBase, table=True):
    __tablename__ = 'language_certificates'    
    job_id: int = Field(default=None, foreign_key="job_descriptions.id")
    language: str = Field(default=None)
    language_certificate_name: str = Field(default=None)
    language_certificate_level: str = Field(default=None)
    
class OtherCertificate(TableBase, table=True):
    __tablename__ = 'other_certificates'    
    job_id: int = Field(default=None, foreign_key="job_descriptions.id")
    certificate_name: str = Field(default=None)
    certificate_level: str = Field(default=None)


class Industry(TableBase, table=True):
    __tablename__ = 'industries'
    job_id: int = Field(default=None, foreign_key="job_descriptions.id")
    name: str = Field(default=None)


class ResumeOld(TableBase, table=True):
    __tablename__ = 'resume_olds'    
    industry_id: int = Field(default=None, foreign_key="industries.id")
    user_id: int = Field(default=None, foreign_key="users.id")


class ResumeNew(TableBase, table=True):
    __tablename__ = 'resume_news'    
    industry_id: int = Field(default=None, foreign_key="industries.id")
    user_id: int = Field(default=None, foreign_key="users.id")
    job_id: int = Field(default=None, foreign_key="job_descriptions.id")


class ValuationInfo(TableBase, table=True):
    __tablename__ = 'valuation_infos'
    new_id: int = Field(default=None, foreign_key="resume_news.id")
    old_id: int = Field(default=None, foreign_key="resume_olds.id")
    hard: str = Field(default=None)
    hard_point: float = Field(default=None)
    degrees: List[str] = Field(default=None, sa_column=Column(TEXT))
    degree_point: float = Field(default=None)
    certificates: List[str] = Field(default=None, sa_column=Column(TEXT))
    certificates_point: float = Field(default=None)
    total_point: float = Field(default=None)


class ResumeVersion(TableBase, table=True):
    __tablename__ = 'resume_versions'

    old_id: int = Field(default=None, foreign_key="resume_olds.id")
    new_id: int = Field(default=None, foreign_key="resume_news.id")
    filename: str = Field(default=None)
    is_lastest: bool = Field(default=True)
    cv_file: str = Field(default=None)
    name: str = Field(default=None) 
    avatar: str = Field(default=None) 
    level: str = Field(default=None) 
    gender: str = Field(default=None)
    current_job: str = Field(default=None)
    skills: List[str] = Field(default=None, sa_column=Column(postgresql.ARRAY(String())))
    current_job_industry: str = Field(default=None)
    email: str = Field(default=None)
    phone: str = Field(default=None)  
    address: str = Field(default=None, sa_column=Column(TEXT))
    city: str = Field(default=None)
    country: str = Field(default=None)  
    description: str = Field(default=None, sa_column=Column(TEXT))
    birthday: str = Field(default=None)
    identification_code: str = Field(default=None, unique=True)
    linkedin: Optional[str] = Field(default=None)
    website: Optional[str] = Field(default=None)
    facebook: Optional[str] = Field(default=None)
    instagram: Optional[str] = Field(default=None)
    status: str = Field(default="pending")
    package: str = Field(default=None)
    objectives: str = Field(default=None)
    is_valuate: bool = Field(default=False)
    is_ai_matching: bool = Field(default=False)
    is_admin_matching: bool = Field(default=False)
    matching_decline_reason: str = Field(default=None, sa_column=Column(TEXT))


class ResumeEducation(TableBase, table=True):
    __tablename__ = 'resume_educations'
    cv_id: int = Field(default=None, foreign_key="resume_versions.id")
    degree: str = Field(default=None)
    institute_name: str = Field(default=None)
    major: str = Field(default=None)
    gpa: str = Field(default=None)
    start_time: datetime = Field(default=None)
    end_time: datetime = Field(default=None)

class ResumeExperience(TableBase, table=True):
    __tablename__ = 'resume_experiences'
    cv_id: int = Field(default=None, foreign_key="resume_versions.id")
    company_name: str = Field(default=None)
    job_tile: str = Field(default=None)
    working_industry: str = Field(default=None)
    levels: str = Field(default=None)
    roles: str = Field(default=None)
    start_time: datetime = Field(default=None)
    end_time: datetime = Field(default=None)

class ResumeAward(TableBase, table=True):
    __tablename__ = 'resume_awards'
    cv_id: int = Field(default=None, foreign_key="resume_versions.id")
    name: str = Field(default=None)
    time: str = Field(default=None)
    description: str = Field(default=None, sa_column=Column(TEXT))

class ResumeProject(TableBase, table=True):
    __tablename__ = 'resume_projects'
    cv_id: int = Field(default=None, foreign_key="resume_versions.id")
    project_name: str = Field(default=None)
    description: str = Field(default=None)
    start_time: datetime = Field(default=None)
    end_time: datetime = Field(default=None)