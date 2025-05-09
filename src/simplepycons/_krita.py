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


class KritaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "krita"

    @property
    def original_file_name(self) -> "str":
        return "krita.svg"

    @property
    def title(self) -> "str":
        return "Krita"

    @property
    def primary_color(self) -> "str":
        return "#3BABFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Krita</title>
     <path d="M.652.76a.625.625 0 00-.5.246c-.352.448-.035.898.362
 1.262.206.189 1.77 1.794 3.428 3.527a11.054 11.054 0
 011.815-1.983C3.667 2.515 1.694 1.266 1.461 1.1
 1.201.914.917.762.652.76zm5.105 3.052c1.848 1.148 3.786 2.332 4.693
 2.84 1.469.821 3.758 2.684 4.092 4.434.535.466 2.182 1.916 2.596
 2.413.698-.211 1.518.133 2.06 1.12.866 1.583.227 3.747-1.968
 4.988a5.42 5.42 0
 01-.296.267l.296-.267c1.14-1.468-.714-2.44-1.175-3.864a2.06 2.06 0
 01-.11-.78c-.533-.282-2.11-1.452-2.795-1.965-1.801.16-4.207-1.773-5.35-3.08-.7-.802-2.32-2.517-3.858-4.123a11.052
 11.052 0 00-2.046 6.393A11.052 11.052 0 1012.948
 1.136c-2.64.004-5.19.954-7.19 2.676zm8.71
 7.552c-.515.126-.968.831-1.118 1.306-.038.115-.04.303.066.342.802.592
 1.556 1.168 2.4 1.7.162-.393.746-.963 1.096-1.2zm-11.53 1.639c.812
 1.898 5.798 7.17 12.06 2.695a2.07 2.07 0 00.114.715c.46 1.42 2.36
 2.427 1.238 3.89-2.135 1.364-5
 1.201-6.989.528-3.558-1.204-5.914-4.332-6.424-7.828zm13.782.7a.771.771
 0
 00-.065.049c-.004.003-.008.008-.011.008.003-.003.007-.008.01-.008.024-.015.044-.034.066-.048z"
 />
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
