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


class SonarqubeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sonarqube"

    @property
    def original_file_name(self) -> "str":
        return "sonarqube.svg"

    @property
    def title(self) -> "str":
        return "SonarQube"

    @property
    def primary_color(self) -> "str":
        return "#4E9BCD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SonarQube</title>
     <path d="M15.685.386l-.465.766c3.477 2.112 6.305 5.27 7.966
 8.89L24 9.67C22.266 5.887 19.313 2.59 15.685.386zM8.462.91l-.305
 1.075c6.89 1.976 12.384 7.64 13.997 14.421l1.085-.258C21.535 8.977
 15.735 2.997 8.462.909zM0 2.667v1.342c10.963 0 19.883 8.795 19.883
 19.605h1.342c0-11.55-9.522-20.947-21.225-20.947z" />
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
