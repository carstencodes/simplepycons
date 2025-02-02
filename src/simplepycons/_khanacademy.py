#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class KhanAcademyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "khanacademy"

    @property
    def original_file_name(self) -> "str":
        return "khanacademy.svg"

    @property
    def title(self) -> "str":
        return "Khan Academy"

    @property
    def primary_color(self) -> "str":
        return "#14BF96"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Khan Academy</title>
     <path d="M21.724 4.973L13.418.328a3.214 3.214 0 0 0-2.828 0L2.276
 4.973A3.05 3.05 0 0 0 .862 7.371v9.256a3.05 3.05 0 0 0 1.414
 2.4l8.306 4.645a3.214 3.214 0 0 0 2.828 0l8.314-4.645a3.05 3.05 0 0 0
 1.414-2.4V7.373a3.05 3.05 0 0 0-1.414-2.4zM12 4.921a2.571 2.571 0 1 1
 .001 5.143A2.571 2.571 0 0 1 12 4.92zm3.094 13.627a9.119 9.119 0 0
 1-3.103.549 8.972 8.972 0 0 1-3.076-.55 8.493 8.493 0 0
 1-5.486-7.987v-.857c4.646.017 8.074 3.823 8.074
 8.51v.198h.926v-.197c0-4.688 3.445-8.51
 8.056-8.51.026.29.043.582.086.856a8.502 8.502 0 0 1-5.477 7.988z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://support.khanacademy.org/hc/en-us/arti'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://khanacademy.zendesk.com/hc/en-us/arti'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
