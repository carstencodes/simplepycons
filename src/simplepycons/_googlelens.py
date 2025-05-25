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


class GoogleLensIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlelens"

    @property
    def original_file_name(self) -> "str":
        return "googlelens.svg"

    @property
    def title(self) -> "str":
        return "Google Lens"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Lens</title>
     <path d="M12 17.333q-1.667 0-2.833-1.166Q8 15 8 13.333q0-1.666
 1.167-2.833Q10.333 9.333 12 9.333q1.667 0 2.833 1.167Q16 11.667 16
 13.333q0 1.667-1.167 2.834-1.166 1.166-2.833 1.166Zm8 5.334q-1.1
 0-1.883-.784-.784-.783-.784-1.883t.784-1.883q.783-.784
 1.883-.784t1.883.784q.784.783.784 1.883t-.784
 1.883q-.783.784-1.883.784ZM5.333 24q-2.2 0-3.766-1.567Q0 20.867 0
 18.667V16h2.667v2.667q0 1.1.783 1.883.783.783
 1.883.783H12V24Zm16-10.667V8q0-1.1-.783-1.883-.783-.784-1.883-.784H5.333q-1.1
 0-1.883.784Q2.667 6.9 2.667 8v4H0V8q0-2.2 1.567-3.767 1.566-1.566
 3.766-1.566H8L9.333 0h5.334L16 2.667h2.667q2.2 0 3.766 1.566Q24 5.8
 24 8v5.333z" />
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
