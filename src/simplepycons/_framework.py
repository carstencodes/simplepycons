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


class FrameworkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "framework"

    @property
    def original_file_name(self) -> "str":
        return "framework.svg"

    @property
    def title(self) -> "str":
        return "Framework"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Framework</title>
     <path d="M23.186 9.07 21.41 8.019a2.78 2.78 0 0
 1-1.344-2.391V3.523c0-.431-.19-.837-.516-1.108A11.965 11.965 0 0 0
 16.317.493a1.356 1.356 0 0 0-1.193.091L13.347 1.64a2.622 2.622 0 0
 1-2.688 0L8.882.584a1.348 1.348 0 0 0-1.194-.09 11.93 11.93 0 0
 0-3.231 1.918 1.44 1.44 0 0 0-.516 1.108v2.104c0 .986-.51 1.897-1.344
 2.392L.823 9.068c-.363.215-.61.588-.675 1.013A12.24 12.24 0 0 0 0
 12.001c0 .651.048 1.292.145 1.916.065.425.312.801.675 1.016l1.774
 1.052a2.78 2.78 0 0 1 1.344 2.392v2.104c0 .431.191.837.516
 1.108.965.8 2.054 1.452 3.231 1.919.393.155.831.124
 1.194-.091l1.777-1.055a2.622 2.622 0 0 1 2.688 0l1.777
 1.055c.363.215.804.246 1.193.091a11.973 11.973 0 0 0 3.232-1.92 1.44
 1.44 0 0 0 .516-1.107v-2.104a2.78 2.78 0 0 1
 1.344-2.392l1.774-1.052c.363-.215.61-.588.675-1.016.094-.624.145-1.265.145-1.916
 0-.652-.048-1.293-.145-1.917a1.41 1.41 0 0 0-.67-1.013zM12.003
 19.41c-3.981 0-7.21-3.317-7.21-7.407s3.229-7.406 7.21-7.406c3.98 0
 7.21 3.316 7.21 7.406s-3.23 7.407-7.21 7.407z" />
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
