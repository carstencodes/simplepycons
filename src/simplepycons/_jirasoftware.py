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


class JiraSoftwareIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jirasoftware"

    @property
    def original_file_name(self) -> "str":
        return "jirasoftware.svg"

    @property
    def title(self) -> "str":
        return "Jira Software"

    @property
    def primary_color(self) -> "str":
        return "#0052CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Jira Software</title>
     <path d="M12.004 0c-2.35 2.395-2.365 6.185.133 8.585l3.412
 3.413-3.197 3.198a6.501 6.501 0 0 1 1.412 7.04l9.566-9.566a.95.95 0 0
 0 0-1.344L12.004 0zm-1.748 1.74L.67 11.327a.95.95 0 0 0 0 1.344C4.45
 16.44 8.22 20.244 12 24c2.295-2.298 2.395-6.096-.08-8.533l-3.47-3.469
 3.2-3.2c-1.918-1.955-2.363-4.725-1.394-7.057z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.atlassian.com/company/news/press-'''

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
