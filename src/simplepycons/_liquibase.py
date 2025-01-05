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


class LiquibaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "liquibase"

    @property
    def original_file_name(self) -> "str":
        return "liquibase.svg"

    @property
    def title(self) -> "str":
        return "Liquibase"

    @property
    def primary_color(self) -> "str":
        return "#2962FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Liquibase</title>
     <path d="M12.01884 0C6.64997 0 2.96561 1.92248 2.96477 3.64555c0
 1.72307 3.7271 3.64555 9.05571 3.64555 5.32776 0 9.05407-1.92248
 9.05407-3.64555S17.34745 0 12.01885 0Zm9.0557 6.45057c-1.60226
 1.28266-3.48576 1.72252-7.33205 2.64446-5.3286 1.24155-10.81704
 2.5238-10.81704 7.53195v.56035c2.00297-1.72282 5.60817-2.5234
 9.13435-3.32441h.0016c4.40704-1.00153 9.01311-2.04399
 9.01311-4.60732zm0 5.84927c-1.92272 1.56284-5.328 2.32433-8.6936
 3.0852-4.64743 1.0419-9.45549 2.123-9.45549 5.0071 0 .64174.52143
 1.3229 1.4828 1.92353 1.92356-1.28181 4.92803-2.0026 7.81212-2.68377
 4.36724-1.04106 8.85418-2.12278 8.85418-4.80721zm0 5.64937c-1.88329
 1.60227-5.2489 2.40461-8.49371 3.16548-2.36398.56206-4.76777
 1.1223-6.45057 1.96286C7.65283 23.63961 9.69593 24 12.02048
 24c5.28834 0 9.05407-1.88469 9.05407-3.64719z" />
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
