#This file is part jasper_reports module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.

from trytond.pool import Pool
from .data_template import *
from .model import *
from .sequence import *
from .translation import *


def register():
    Pool.register(
        DataTemplateStart,
        DataTemplateResult,
        Model,
        Translation,
        module='jasper_reports', type_='model')
    Pool.register(
        DataTemplate,
        ReportTranslationSet,
        TranslationUpdate,
        TranslationClean,
        module='jasper_reports', type_='wizard')
    Pool.register(
        SequenceReport,
        module='jasper_reports', type_='report')
