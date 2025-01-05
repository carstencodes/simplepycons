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


class RockyLinuxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rockylinux"

    @property
    def original_file_name(self) -> "str":
        return "rockylinux.svg"

    @property
    def title(self) -> "str":
        return "Rocky Linux"

    @property
    def primary_color(self) -> "str":
        return "#10B981"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rocky Linux</title>
     <path d="M23.332 15.957c.433-1.239.668-2.57.668-3.957
 0-6.627-5.373-12-12-12S0 5.373 0 12c0 3.28 1.315 6.251 3.447
 8.417L15.62 8.245l3.005 3.005zm-2.192 3.819l-5.52-5.52L6.975
 22.9c1.528.706 3.23 1.1 5.025 1.1 3.661 0 6.94-1.64 9.14-4.224z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/rocky-linux/branding/blob/'''

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
