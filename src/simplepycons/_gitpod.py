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


class GitpodIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gitpod"

    @property
    def original_file_name(self) -> "str":
        return "gitpod.svg"

    @property
    def title(self) -> "str":
        return "Gitpod"

    @property
    def primary_color(self) -> "str":
        return "#FFAE33"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gitpod</title>
     <path d="M14.033 1.195a2.387 2.387 0 0 1-.87 3.235l-6.98
 4.04a.602.602 0 0 0-.3.522v6.342a.6.6 0 0 0 .3.521l5.524
 3.199a.585.585 0 0 0 .586 0l5.527-3.199a.603.603 0 0 0
 .299-.52V11.39l-4.969 2.838a2.326 2.326 0 0 1-3.19-.9 2.388 2.388 0 0
 1 .89-3.23l7.108-4.062C20.123 4.8 22.8 6.384 22.8 8.901v6.914a4.524
 4.524 0 0 1-2.245 3.919l-6.345 3.672a4.407 4.407 0 0 1-4.422
 0l-6.344-3.672A4.524 4.524 0 0 1 1.2 15.816V8.51a4.524 4.524 0 0 1
 2.245-3.918l7.393-4.28a2.326 2.326 0 0 1 3.195.883z" />
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
