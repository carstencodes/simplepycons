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


class ApacheSolrIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apachesolr"

    @property
    def original_file_name(self) -> "str":
        return "apachesolr.svg"

    @property
    def title(self) -> "str":
        return "Apache Solr"

    @property
    def primary_color(self) -> "str":
        return "#D9411E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apache Solr</title>
     <path d="M20.741 3.8L8.926 16.573l14.849-6.851A11.979 11.979 0 0
 0 20.741 3.8M11.975 0c-1.637 0-3.197.328-4.619.921l-1.585
 13.36L13.693.124A12.168 12.168 0 0 0 11.975 0m11.918 10.459l-14.07
 7.874 13.201-1.566a11.976 11.976 0 0 0 .869-6.308m-5.188
 11.527a12.084 12.084 0 0 0 3.8-4.16l-12.374 2.457 8.574
 1.703zM14.417.249L7.53 15.177 20.306 3.36A11.978 11.978 0 0 0
 14.417.249M12.98 24a11.938 11.938 0 0 0 3.774-.945l-6.931-.822L12.98
 24zM1.016 7.08a11.944 11.944 0 0 0-1.013 3.864l1.867
 3.337-.854-7.201zm5.298-5.665a12.076 12.076 0 0 0-4.236 3.784l1.743
 8.773L6.314 1.415z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
