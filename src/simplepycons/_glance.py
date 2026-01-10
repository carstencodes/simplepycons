#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class GlanceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "glance"

    @property
    def original_file_name(self) -> "str":
        return "glance.svg"

    @property
    def title(self) -> "str":
        return "Glance"

    @property
    def primary_color(self) -> "str":
        return "#D9C38C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Glance</title>
     <path d="M2.77 0A2.763 2.763 0 0 0 0 2.77v18.46A2.763 2.763 0 0 0
 2.77 24h18.46A2.763 2.763 0 0 0 24 21.23V2.77A2.763 2.763 0 0 0 21.23
 0Zm.922 1.846h5.539c1.023 0 1.846.824 1.846 1.846v16.616a1.842 1.842
 0 0 1-1.846 1.846H3.692a1.842 1.842 0 0
 1-1.846-1.846V3.692c0-1.022.824-1.846 1.846-1.846zm11.077
 0h5.539c1.022 0 1.846.824 1.846 1.846v5.539a1.842 1.842 0 0 1-1.846
 1.846h-5.539a1.842 1.842 0 0 1-1.846-1.846V3.692c0-1.022.823-1.846
 1.846-1.846zm1.226 1.846-.946.961h2.964c.148 0
 .29-.005.423-.012a.78.78 0 0 0 .312-.089L14.77 8.528l.725.703
 3.923-3.941a1.031 1.031 0 0 0-.1.322 3.265 3.265 0 0
 0-.023.38v3.071l1.014-1.004V3.692Zm-1.226 9.231h5.539c1.022 0
 1.846.823 1.846 1.846v5.539a1.842 1.842 0 0 1-1.846
 1.846h-5.539a1.842 1.842 0 0 1-1.846-1.846v-5.539c0-1.023.823-1.846
 1.846-1.846z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/glanceapp/glance/blob/c88f
d526e55117445c7f4440c83b661faa402047/internal/glance/static/favicon.sv'''

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
