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


class KSixIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "k6"

    @property
    def original_file_name(self) -> "str":
        return "k6.svg"

    @property
    def title(self) -> "str":
        return "k6"

    @property
    def primary_color(self) -> "str":
        return "#7D64FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>k6</title>
     <path d="M24 23.646H0L7.99 6.603l4.813
 3.538L19.08.354Zm-8.8-3.681h.052a2.292 2.292 0 0 0 1.593-.64 2.088
 2.088 0 0 0 .685-1.576 1.912 1.912 0 0 0-.66-1.511 2.008 2.008 0 0
 0-1.37-.59h-.04a.716.716 0 0
 0-.199.027l1.267-1.883-1.01-.705-.477.705-1.22
 1.864c-.21.31-.386.582-.495.77-.112.2-.21.41-.29.625a1.942 1.942 0 0
 0-.138.719 2.086 2.086 0 0 0 .676 1.558c.422.411.989.641
 1.578.64Zm-5.365-2.027 1.398 1.978h1.496l-1.645-2.295
 1.46-2.029-.97-.671-.427.565-1.314
 1.853v-3.725l-1.31-1.068v7.37h1.31v-1.98Zm5.367.792a.963.963 0 1 1
 0-1.927h.009a.941.941 0 0 1 .679.29.897.897 0 0 1 .29.668.978.978 0 0
 1-.977.967Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:K6-lo'''

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
        yield from [
            "Grafana k6",
        ]
