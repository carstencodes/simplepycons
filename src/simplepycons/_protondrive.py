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


class ProtonDriveIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "protondrive"

    @property
    def original_file_name(self) -> "str":
        return "protondrive.svg"

    @property
    def title(self) -> "str":
        return "Proton Drive"

    @property
    def primary_color(self) -> "str":
        return "#EB508D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Proton Drive</title>
     <path d="M24 6.595v12.79c0 1.36-1.11 2.462-2.482
 2.462h-1.62V9a2.925 2.925 0 0 0-2.93-2.914l-9.42.053a.943.943 0 0
 1-.55-.172L4.905 4.493a2.918 2.918 0 0 0-1.694-.536H.1A2.47 2.47 0 0
 1 2.482 2.15h4.657c.47 0 .928.148 1.305.424l1.559
 1.134c.38.276.837.424 1.308.424h10.207A2.471 2.471 0 0 1 24
 6.595zM18.897 9v12.85H2.482A2.471 2.471 0 0 1 0 19.387V4.957h3.21c.4
 0 .792.122 1.118.353l2.095 1.476a1.94 1.94 0 0 0
 1.13.353l9.402-.052A1.922 1.922 0 0 1 18.897 9z" />
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
