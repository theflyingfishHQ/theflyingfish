# Copyright (c) 2025, Simon Wanyama and contributors
# For license information, please see license.txt

import frappe
from frappe.website.utils import find_first_image, get_html_content_based_on_type
from frappe.utils import strip_html_tags, cint
from frappe.website.website_generator import WebsiteGenerator

class JobVacancy(WebsiteGenerator):
	def before_save(self):
		self.route = "job-vacancies/{}".format(self.name)

	def get_context(self, context):
		# this is for double precaution. usually it wont reach this code if not published
		if not cint(self.is_published):
			raise Exception("This Vacancy has not been published yet!")

		description = self.vacancy_details[:500] if self.vacancy_details else self.vacancy_title
		context.description = description

		context.metatags = {
			"name": self.vacancy_title,
			"description": context.description,
		}

		context.metatags["image"] = self.cover_image or None
